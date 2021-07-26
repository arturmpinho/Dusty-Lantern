from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product



# Create your views here.

@login_required
def profile(request):
    """ Display the user's profile"""

    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = "profiles/profile.html"
    context = {
        "user_profile": user_profile,
        'form': form,
        'orders': orders
    }
    
    return render(request, template, context)

@login_required
def order_history(request, order_number):
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
def add_product(request):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            return redirect('add_auction', args=[product.id])

        else:
            print(product_form.errors)
            messages.error(request, "Failed to add product. \
            Please ensure the form is valid.")
    else:
        product_form = ProductForm()
        template = 'profiles/add_product.html'

        context = {
            'product_form': product_form
        }
        return render(request, template, context)



@login_required
def add_auction(request, product_id):
    """ Function for superuser to add auction"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    print(product_id)

    auction_form = AuctionForm()

    template = "profiles/add_auction.html"
    context = {
        'auction_form': auction_form,
    }

    return render(request, template, context)