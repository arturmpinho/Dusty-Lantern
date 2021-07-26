from django.shortcuts import render, get_object_or_404, redirect, reverse
# from .models import UserProfile
from .forms import AuctionForm, ProductForm
# from checkout.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from products.models import Product



# Create your views here.

def auctions(request):

    template = "auctionsmng/auctions.html"

    return render(request, template)


def products(request):

    template = "auctionsmng/products.html"

    return render(request, template)


@login_required
def add_product(request):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('products')

        else:
            print(product_form.errors)
            messages.error(request, "Failed to add product. \
            Please ensure the form is valid.")
    else:
        product_form = ProductForm()
        template = 'auctionsmng/add_product.html'

        context = {
            'product_form': product_form
        }
        return render(request, template, context)



@login_required
def add_auction(request):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    auction_form = AuctionForm()

    template = "auctionsmng/add_auction.html"
    context = {
        'auction_form': auction_form,
    }

    return render(request, template, context)
