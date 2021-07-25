from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


# Create your views here.


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
    print(orders)

    template = "profiles/profile.html"
    context = {
        "user_profile": user_profile,
        'form': form,
        'orders': orders
    }
    
    return render(request, template, context)