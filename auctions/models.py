from django.db import models
from products.models import Product, Image


class Auction(models.Model):

    product = models.ForeignKey(Product, null=True,
                                on_delete=models.CASCADE)
    base_amount = models.DecimalField(max_digits=7, decimal_places=2)
    bidding_increment = models.DecimalField(max_digits=4, decimal_places=2)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()

    def __str__(self):
        return self.product
