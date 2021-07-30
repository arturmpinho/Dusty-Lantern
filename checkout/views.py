from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import json
import stripe


from .forms import OrderForm
from .models import Order, OrderLineItem

from auctions.models import Bag, Auction, Bid
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = Bag.objects.filter(bidder=request.user)
        checkout_bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            for auction_id, bid_id in checkout_bag.items():
                try:
                    auction = Auction.objects.get(id=auction_id)
                    bid = Bid.objects.get(id=bid_id)
                    if isinstance(bid_id, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            auction=auction,
                            lineitem_total=bid.bid,
                        )
                        order_line_item.save()
                except Auction.DoesNotExist:
                    messages.error(request, (
                        "Error"
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_profile'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('\
                checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # Ensure bag in session is cleared out before creating new session bag
    if 'bag' in request.session:
        del request.session['bag']

    bag = Bag.objects.filter(bidder=request.user)
    checkout_bag = request.session.get('bag', {})
    auctions = []
    bids = []
    order_total = 0
    auction_fee = 0
    for item in bag:
        auction = get_object_or_404(Auction, pk=item.auction.id)
        bid = get_object_or_404(Bid, pk=item.bid.id)
        checkout_bag[item.auction.id] = item.bid.id
        order_total += bid.bid
        auctions.append(auction)
        bids.append(bid)
    request.session['bag'] = checkout_bag

    if order_total < 500:
        auction_fee = float(order_total) * 0.05
    elif order_total < 1000:
        auction_fee = float(order_total) * 0.025
    else:
        auction_fee = float(order_total) * 0.01

    grand_total = float(order_total) + auction_fee

    stripe_total = round(grand_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Attempt to prefill the form with any info
    # that the user maintains in their profile
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'first_name': request.user.first_name,
                'last_name': user_profile.user.last_name,
                'email': user_profile.user.email,
                'phone_number': user_profile.default_phone_number,
                'country': user_profile.default_country,
                'postcode': user_profile.default_postcode,
                'town_or_city': user_profile.default_town_or_city,
                'street_address1': user_profile.default_street_address1,
                'street_address2': user_profile.default_street_address2,
                'county': user_profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe Public Key is missing.  \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
            'auctions': auctions,
            'bids': bids,
            'order_total': order_total,
            'grand_total': grand_total,
            'auction_fee': auction_fee,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = user_profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data,
                                                instance=user_profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    bag = Bag.objects.filter(bidder=request.user)
    for item in bag:
        item.delete()

    if 'bag' in request.session:
        del request.session['bag']

    for item in order.lineitems.all():
        auction = Auction.objects.get(pk=item.auction.id)
        auction.is_sold = True
        auction.save()

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
