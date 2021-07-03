from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Auction(models.Model):

    product = models.ForeignKey(Product, null=True,
                                on_delete=models.CASCADE)
    base_amount = models.DecimalField(max_digits=7, decimal_places=2)
    bidding_increment = models.DecimalField(max_digits=7, decimal_places=2)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def __str__(self):
        return self.product.title


class Bid(models.Model):
    bidder = models.ForeignKey(User,
                               null=True, blank=False,
                               on_delete=models.SET_NULL)
    auction = models.ForeignKey(Auction, null=True,
                                on_delete=models.CASCADE)
    bidding_time = models.DateTimeField()
    bid = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.bid
