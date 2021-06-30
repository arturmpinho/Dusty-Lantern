from django.contrib import admin
from .models import Auction


class AuctionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'base_amount',
        'bidding_increment',
        'start_date_time',
        'end_date_time',
    )

    ordering = ('start_date_time',)


admin.site.register(Auction, AuctionAdmin)
