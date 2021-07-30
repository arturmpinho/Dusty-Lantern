import uuid

from django.db import models

from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from auctions.models import Auction
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False,
                              default="")
    phone_number = models.CharField(max_length=20,
                                    null=False, blank=False)
    street_address1 = models.CharField(max_length=80,
                                       null=False, blank=False)
    street_address2 = models.CharField(max_length=80,
                                       null=True, blank=True)
    postcode = models.CharField(max_length=20,
                                null=False, blank=False)
    town_or_city = models.CharField(max_length=40,
                                    null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *',
                           null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    auction_fee = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random unique order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time an auction is added
        to the bag, including the auction fee.
        """
        self.order_total = self.lineitems.aggregate(Sum('\
            lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < 500:
            self.auction_fee = float(self.order_total) * 0.05
        elif self.order_total < 1000:
            self.auction_fee = float(self.order_total) * 0.025
        else:
            self.auction_fee = float(self.order_total) * 0.01
        self.grand_total = float(self.order_total) + self.auction_fee
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    auction = models.ForeignKey(Auction, null=False, blank=False,
                                on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=7, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def __str__(self):
        return self.auction.product.title
