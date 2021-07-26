from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctions, name='auctions'),
    path('products', views.products, name='products'),
    path('add_product', views.add_product, name='add_product'),
    path('add_auction', views.add_auction, name='add_auction')
]
