import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from auctions.models import Auction, Bid, Bag
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile"""

    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    # when user updates profile, save it to the database
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Failed to update profile. \
            Please ensure the form is valid.')
            return redirect('profile')

    form = UserProfileForm(instance=user_profile)

    # Get all the past orders for this user
    orders = user_profile.orders.all()

    now = datetime.datetime.now()
    unique_auctions = []
    winning_bids = []

    # Get all the bids of the user
    bids = Bid.objects.filter(bidder=user)

    # For each bid, get the corresponding auction if the auction is closed
    for bid in bids:
        auctions = Auction.objects.filter(pk=bid.auction.id)
        for auction in auctions:
            if auction.end_date_time.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4] < now.strftime('%Y-%m-%d %H:%M:%S.%s')[:-4]:
                # Append auction to the unique auctions if it's not in there yet
                if auction not in unique_auctions:
                    unique_auctions.append(auction)

    # For each auction in unique auctions, get the highest bid
    for auction in unique_auctions:
        all_bids = Bid.objects.filter(auction=auction.id)
        if all_bids:
            highest_bid = all_bids.order_by('-bidding_time')[0]

            # Check if the highest bid for the auctions corresponds to one of bids of the user
            if highest_bid in bids:
                winning_auction = Auction.objects.get(
                    pk=highest_bid.auction.id)
                # Check if the user hasn't already paid for this item by checking the is_sold field
                if winning_auction.is_sold is not True:
                    winning_bids.append(highest_bid)

    template = "profiles/profile.html"
    context = {
        "user_profile": user_profile,
        'form': form,
        'orders': orders,
        'winning_bids': winning_bids
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Display's the order history of specific order
    with reminding message that this is a past order.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'This is a past confirmation for order number {order_number} \
        A confirmation email was sent on the order date')

    template = "checkout/checkout_success.html"

    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, template, context)


@login_required
def add_to_cart(request, auction_id):
    """ Add auction to cart"""

    auction = get_object_or_404(Auction, pk=auction_id)
    bids = Bid.objects.filter(auction=auction.id)

    if bids:
        highest_bid = bids.order_by('-bidding_time')[0]
        bidder = highest_bid.bidder

        # Ensure there is no other bag for this user to ensure proceeding
        # checkout with 1 auction only
        expired_bag = Bag.objects.filter(bidder=highest_bid.bidder)
        if expired_bag:
            for item in expired_bag:
                item.delete()

        # Create bag with correct auction, bid and bidder
        bag = Bag(
            auction=auction,
            bid=highest_bid,
            bidder=bidder
        )
        bag.save()

        return redirect(reverse('checkout'))
