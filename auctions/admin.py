from django.contrib import admin


class AuctionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'base_amount',
        'number_of_bids',
        'bidding_increment',
        'start_date_time',
        'end_date_time',
    )
