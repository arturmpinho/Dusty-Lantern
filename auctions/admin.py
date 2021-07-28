from django.contrib import admin
from .models import Auction, Bid, Bag


class BidAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'auction',
        'bidder',
        'bidding_time',
        'bid',
    )


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


class BagAdmin(admin.ModelAdmin):

    list_display = (
        'auction',
        'bid',
        'bidder',
    )


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Bag, BagAdmin)
