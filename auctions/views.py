from django.shortcuts import render
from .models import Auction


def all_auctions(request):
    """View to return the auctions page w/ sorting and search queries"""

    auctions = Auction.objects.all()

    context = {
        'auctions': auctions,
    }

    return render(request, 'auctions/auctions.html', context)
