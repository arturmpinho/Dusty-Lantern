import json
import time

from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from profiles.models import UserProfile
from auctions.models import Auction, Bid, Bag
from .models import Order, OrderLineItem


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Save user info when set to True
        user_profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            user_profile = UserProfile.objects.get(user__username=username)
            if save_info != "false":
                user_profile.default_phone_number = shipping_details.phone
                user_profile.default_country = shipping_details.address.country
                user_profile.default_postcode = (shipping_details.
                                                 address.postal_code)
                user_profile.default_town_or_city = (shipping_details.
                                                     address.city)
                user_profile.default_street_address1 = (shipping_details.
                                                        address.line1)
                user_profile.default_street_address2 = (shipping_details.
                                                        address.line2)
                user_profile.default_county = shipping_details.address.state
                user_profile.save()

        # Check if the order already exists in the database for 5 times
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name.split(' ')[0],
                    last_name=shipping_details.name.split(' ')[1:-1],
                    user_profile=user_profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    stripe_pid=pid,
                )
                for auction_id, bid_id in json.loads(bag).items():
                    auction = Auction.objects.get(id=auction_id)
                    bid = Bid.objects.get(id=bid_id)
                    if isinstance(bid_id, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            auction=auction,
                            lineitem_total=bid.bid,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Remove all bags for user
        bag = Bag.objects.filter(bidder=user_profile.user)
        for item in bag:
            item.delete()

        # Set the auction to is_sold
        for item in order.lineitems.all():
            auction = Auction.objects.get(pk=item.auction.id)
            auction.is_sold = True
            auction.save()

        self._send_confirmation_email(order)

        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
