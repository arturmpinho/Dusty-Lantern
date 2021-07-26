from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import AuctionForm, ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from auctions.models import Auction


# Create your views here.
@login_required
def auctions(request):
    """ Function to display all the auctions for the superuser """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    auctions = Auction.objects.all()
    template = "auctionsmng/auctions.html"
    
    context = {
        'auctions': auctions
    }

    return render(request, template, context)


@login_required
def products(request):
    """ Function to display all the products for the superuser """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    products = Product.objects.all()
    template = "auctionsmng/products.html"
    
    context = {
        'products': products
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            messages.info(request, f'Product {product} has been successfully added!')
            return redirect('products')

        else:
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
def delete_product(request, product_id):
    """
    Function to delete the product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted')
    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    """
    Function to edit the product for superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES,
                                   instance=product)
        if product_form.is_valid:
            product = product_form.save()
            messages.info(request, f'You have successfully updated \
                product {product}.')
            return redirect('products')
        else:
            messages.error(request, 'Failed to update product. \
            Please ensure the form is valid.')
            
    product_form = ProductForm(instance=product)
    messages.info(request, f'You are editing product: \
         {product}')

    template = 'auctionsmng/edit_product.html'

    context = {
        'product_form': product_form,
        'product': product
    }
    return render(request, template, context)


@login_required
def add_auction(request):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        auction_form = AuctionForm(request.POST)
        if auction_form.is_valid():
            auction = auction_form.save()
            messages.info(request, f'Auction {auction} has been successfully added!')
            return redirect('auctions')

        else:
            messages.error(request, "Failed to add auction. \
            Please ensure the form is valid.")
    else:
        auction_form = AuctionForm()
        template = 'auctionsmng/add_auction.html'

        context = {
            'auction_form': auction_form
        }
        return render(request, template, context)


@login_required
def edit_auction(request, auction_id):
    """
    Function to edit the auction for superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))
    
    auction = get_object_or_404(Auction, pk=auction_id)

    if request.method == "POST":
        auction_form = AuctionForm(request.POST,
                                   instance=auction)
        if auction_form.is_valid:
            auction = auction_form.save()
            messages.info(request, f'You have successfully updated \
                auction concerning product {auction}.')
            return redirect('auctions')
        else:
            messages.error(request, 'Failed to update auction. \
            Please ensure the form is valid.')
            
    auction_form = AuctionForm(instance=auction)
    messages.info(request, f'You are editing auction concerning product: \
         {auction}')

    template = 'auctionsmng/edit_auction.html'

    context = {
        'auction_form': auction_form,
        'auction': auction
    }
    return render(request, template, context)


@login_required
def delete_auction(request, auction_id):
    """
    Function to delete the auction
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    auction = get_object_or_404(Auction, pk=auction_id)
    auction.delete()
    messages.success(request, 'Auction successfully deleted')
    return redirect(reverse('auctions'))