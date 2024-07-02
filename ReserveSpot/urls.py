from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.editprofile, name='editprofile'),
    path('reservation/', views.reservation, name='reservation'),
    path('reserveForm/', views.reserveForm, name='reserveForm'),
    path('paymentForm/', views.payment_form, name='paymentForm'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<str:cuisine>/', views.restaurant_list, name='restaurant_list_by_cuisine'),
    path('searchResults/', views.search_results, name='searchResults'),
    path('vendorListings/', views.vendor_listings, name='vendorListings'),
    path('vendorReservations/', views.vendor_reservations, name='vendorReservations'),
    path('vendorTransactions/', views.vendor_transactions, name='vendorTransactions'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('profileProcess/', views.profile_view, name='profile_view')
]