from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm, ProfileForm

import datetime
from django.middleware.csrf import get_token

from ReserveSpot.models import Restaurants

# Create your views here.
def members(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uname']
            password = form.cleaned_data['psw']
            # Authentication logic here
            # Related to DB
            # user = authenticate(request, username=username, password=password) 
            # if user is not None:
            #     login(request, user)
            #     return redirect('profile')
            # else:
            #     form.add_error(None, 'Invalid username or password')

            # Test Login
            if username == 'example' and password == 'password':
                return redirect('profile') # Redirect to profile page after successful login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    
    return render(request, 'home.html', {'login_form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['psw']
             # Save user to database, etc.
            return redirect('profile')  # Redirect to profile page after successful registration
    else:
        form = RegisterForm()
    
    return render(request, 'home.html', {'register_form': form})

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nameinfo']
            email = form.cleaned_data['emailinfo']
            phonenum = form.cleaned_data['phoneinfo']
            password = form.cleaned_data['pwdinfo']
             # Save user to database, etc.
            return redirect('profile')  # Redirect to profile page after successful registration
    else:
        form = RegisterForm()
    
    return render(request, 'editprofile.html', {'profile_form': form})

def about(request):
    return render(request,'about.html')

def profile(request):
    return render(request,'profile.html')

def editprofile(request):
    return render(request,'editprofile.html')

def reservation(request):
    return render(request,'reservation.html')

def reserveForm(request):
    return render(request,'reserveForm.html')

def payment_form(request):
    return render(request, 'paymentForm.html')

def search_results(request): 
    return render(request, 'search_results.html')

def vendor_listings(request):
    return render(request, 'vendor_listings.html')

def vendor_reservations(request):
    return render(request, 'vendor_reservations.html')

def vendor_transactions(request):
    return render(request, 'vendor_transactions.html')

def restaurant_list(request, cuisine=None):
    if cuisine:
        restaurants = Restaurants.objects.filter(cuisine=cuisine)
    else:
        restaurants = Restaurants.objects.all()

    return render(request, 'restaurant_list.html', {'restaurants': restaurants})