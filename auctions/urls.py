from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_auctions, name='auctions'),
    path('<auction_id>', views.auction_detail, name='auction_detail'),
]
