from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_auctions, name='auctions'),
    path('<auction_id>', views.auction_detail, name='auction_detail'),
    path('<auction_id>/place_bid', views.place_bid, name='place_bid'),
    path('<auction_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),
]
