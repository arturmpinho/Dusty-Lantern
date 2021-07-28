from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('<auction_id>/add_to_cart', views.add_to_cart, name='add_to_cart'),

]
