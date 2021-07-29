from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctionsmng, name='auctionsmng'),
    path('products', views.products, name='products'),
    path('add_product', views.add_product, name='add_product'),
    path('add_auction', views.add_auction, name='add_auction'),
    path('<product_id>/edit', views.edit_product,
         name="edit_product"),
    path('<auction_id>/edit', views.edit_auction,
         name="edit_auction"),
    path('products/<product_id>/delete', views.delete_product,
         name="delete_product"),
    path('auctions/<auction_id>/delete', views.delete_auction,
         name="delete_auction"),
]
