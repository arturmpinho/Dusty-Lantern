from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import (AddAuctionForm, AddProductForm,
                    EditAuctionForm, EditProductForm)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product, Image
from auctions.models import Auction
import datetime


# Create your views here.
@login_required
def auctionsmng(request):
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
        product_form = AddProductForm(request.POST, request.FILES)

        images = request.FILES.getlist('images')

        if product_form.is_valid():
            product = product_form.save()
            for image in images:
                Image.objects.create(product=product, image=image)
            images = Image.objects.filter(product=product)
            first_product_image = images[0]
            first_product_image.main_image = True
            first_product_image.save()

            messages.success(request, f'Product {product} has been \
                successfully added!')
            return redirect('products')

        else:
            messages.error(request, "Failed to add product. \
            Please ensure the form is valid.")
    else:
        product_form = AddProductForm()
        template = 'auctionsmng/add_product.html'

        context = {
            'product_form': product_form
        }
        return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Function to delete the product for the superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product successfully deleted')
    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    """
    Function to edit the product for the superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product_form = EditProductForm(request.POST, request.FILES,
                                       instance=product)
        if product_form.is_valid:
            product = product_form.save()
            messages.success(request, f'You have successfully updated \
                product {product}.')
            return redirect('products')
        else:
            messages.error(request, 'Failed to update product. \
            Please ensure the form is valid.')

    product_form = EditProductForm(instance=product)
    product_images = product.images.all()

    messages.info(request, f'You are editing product: \
         {product}')

    template = 'auctionsmng/edit_product.html'

    context = {
        'product_form': product_form,
        'product': product,
        'images': product_images,
    }
    return render(request, template, context)


@login_required
def add_auction(request):
    """ Function for the superuser to add auction"""

    now = datetime.datetime.now()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        auction_form = AddAuctionForm(request.POST)

        if auction_form["start_date_time"].value() > (now.strftime(
                                                     '%Y-%m-%dT%H:%M')):
            if auction_form["end_date_time"].value() > (auction_form[
                                                        "start_date_time\
                                                            "].value()):
                if auction_form.is_valid():
                    auction = auction_form.save()
                    messages.success(request, f'Auction {auction} has been \
                        successfully added!')
                    return redirect('auctionsmng')
                else:
                    messages.error(request, "Failed to add auction. \
                    Please ensure the form is valid.")
            else:
                messages.error(request, "End date time of your action can not be before the start date time. \
                Please adjust the end date time.")
                return redirect(reverse('add_auction'))
        else:
            messages.error(request, "Start time of your action can not be in the past. \
                Please adjust the start date time.")
            return redirect(reverse('add_auction'))
    else:
        auction_form = AddAuctionForm()
        template = 'auctionsmng/add_auction.html'

        context = {
            'auction_form': auction_form
        }
        return render(request, template, context)


@login_required
def edit_auction(request, auction_id):
    """
    Function to edit the auction for the superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    auction = get_object_or_404(Auction, pk=auction_id)

    if request.method == "POST":
        auction_form = EditAuctionForm(request.POST,
                                       instance=auction)
        if auction_form.is_valid:
            auction = auction_form.save()
            messages.success(request, f'You have successfully updated \
                auction concerning product {auction}.')
            return redirect('auctionsmng')
        else:
            messages.error(request, 'Failed to update auction. \
            Please ensure the form is valid.')

    auction_form = EditAuctionForm(instance=auction)
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
    Function to delete the auction for the superuser
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    auction = get_object_or_404(Auction, pk=auction_id)
    auction.delete()
    messages.success(request, 'Auction successfully deleted')
    return redirect(reverse('auctionsmng'))
