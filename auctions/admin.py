from django.contrib import admin
from .models import Auction, Bid


class BidAdmin(admin.TabularInline):

    model = Bid

    list_display = (
        'id',
        'bidder',
        'bidding_time',
        'bid',
    )


class AuctionAdmin(admin.ModelAdmin):
    inlines = [BidAdmin]

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
