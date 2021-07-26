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
