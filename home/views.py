from django.shortcuts import render
from auctions.models import Auction, Bid
import datetime


def index(request):
    """View to return the index page including max 5 ongoing auctions"""

    auctions = Auction.objects.all()
    ongoing_auctions = []
    now = datetime.datetime.now()
    for auction in auctions:
        if auction.start_date_time.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4] < now.strftime('\
            %Y-%m-%d %H:%M:%S.%s')[:-4] and auction.end_date_time.strftime('\
                %Y-%m-%d %H:%M:%S.%s')[:-4] > now.strftime('\
                    %Y-%m-%d %H:%M:%S.%s')[:-4]:
            ongoing_auctions.append(auction)

    top_5 = ongoing_auctions[:4]
    highest_bids = []
    no_bids = []
    for auction in top_5:
        filtered_bids = Bid.objects.filter(auction=auction.id)
        if filtered_bids:
            highest_bid = filtered_bids.order_by('-bidding_time')[0]
            highest_bids.append(highest_bid)
        else:
            no_bids.append(auction)

    context = {
        'auctions': top_5,
        'highest_bids': highest_bids,
        'no_bids': no_bids
    }

    return render(request, 'home/index.html', context)
