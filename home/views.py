from django.shortcuts import render
from auctions.models import Auction
import datetime


def index(request):
    """View to return the index page including max 5 ongoing auctions"""

    auctions = Auction.objects.all()
    ongoing_auctions = []
    now = datetime.datetime.now()
    for auction in auctions:
        if auction.start_date_time.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4] < now.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4] and auction.end_date_time.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4] > now.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4]:
            ongoing_auctions.append(auction)

    top_5 = ongoing_auctions[:4]

    context = {
        'auctions': top_5
    }

    return render(request, 'home/index.html', context)
