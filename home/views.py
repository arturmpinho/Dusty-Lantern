from django.shortcuts import render
from auctions.models import Auction, Bid
import datetime


def index(request):
    """View to return the index page including maximum 4 ongoing auctions"""

    # Get all ongoing auctions 
    auctions = Auction.objects.all()
    ongoing_auctions = []
    now = datetime.datetime.now()
    for auction in auctions:
        if auction.start_date_time.strftime(
            '%Y-%m-%d %H:%M:%S.%s')[:-4] < now.strftime(
            '%Y-%m-%d %H:%M:%S.%s')[:-4] and auction.end_date_time.strftime(
                '%Y-%m-%d %H:%M:%S.%s')[:-4] > now.strftime(
                    '%Y-%m-%d %H:%M:%S.%s')[:-4]:
            ongoing_auctions.append(auction)

    # Assign 4 of the ongoing auctions to top_4
    top_4 = ongoing_auctions[:4]
    highest_bids = []
    no_bids = []

    # For those for auctions, retrieve the current highest bid
    for auction in top_4:
        filtered_bids = Bid.objects.filter(auction=auction.id)
        if filtered_bids:
            # filtering out the hiighest bid by bidding time
            # as latest bid is always be the highest bid.
            highest_bid = filtered_bids.order_by('-bidding_time')[0]
            highest_bids.append(highest_bid)
        else:
            # if no bids, append to no bids in order to display
            # "No bids yet" on the template
            no_bids.append(auction)

    context = {
        'auctions': top_4,
        'highest_bids': highest_bids,
        'no_bids': no_bids
    }

    return render(request, 'home/index.html', context)
