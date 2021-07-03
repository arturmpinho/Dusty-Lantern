from django.shortcuts import render, get_object_or_404
from .models import Auction


def all_auctions(request):
    """View to return the auctions page w/ sorting and search queries"""

    auctions = Auction.objects.all()

    context = {
        'auctions': auctions,
    }

    return render(request, 'auctions/auctions.html', context)


def auction_detail(request, auction_id):
    """View to return the specific details of an auction"""

    auction = get_object_or_404(Auction, pk=auction_id)

    context = {
        'auction': auction,
    }

    return render(request, 'auctions/auction_detail.html', context)
