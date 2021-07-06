from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from django.contrib import messages
from django.db.models import Q
from .models import Auction
from products.models import Category


def all_auctions(request):
    """View to return the auctions page w/ sorting and search queries"""

    auctions = Auction.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                auctions = auctions.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            auctions = auctions.order_by(sortkey)

        if 'category' in request.GET:
            category = request.GET['category']
            auctions = auctions.filter(product__category__name__in=category)
            category = Category.objects.filter(name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "Please check your searching criteria!")
                return redirect(reverse('auctions'))

            queries = (
                        Q(product__title__icontains=query) |
                        Q(product__description__icontains=query)
            )
            auctions = auctions.filter(queries)

    sorting = f'{sort}_{direction}'

    context = {
        'auctions': auctions,
        'search_term': query,
        'category': category,
        'sorting': sorting,
    }

    return render(request, 'auctions/auctions.html', context)


def auction_detail(request, auction_id):
    """View to return the specific details of an auction"""

    auction = get_object_or_404(Auction, pk=auction_id)

    context = {
        'auction': auction,
    }

    return render(request, 'auctions/auction_detail.html', context)
