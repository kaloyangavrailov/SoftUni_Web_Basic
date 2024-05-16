from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, 'common/index.html')


def profile_register(request):
    return render(request, 'profile/profile-login.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


def apartment_details(request):
    return render(request, 'apartment/apartment-details.html')


def apartment_catalogue(request):
    return render(request, 'apartment/apartment-catalogue.html')


def apartment_book(request):
    return render(request, 'apartment/apartment-book.html')


def my_bookings(request):
    return render(request, 'bookings/bookings-details.html')


def booking_edit(request):
    return render(request, 'bookings/booking-edit.html')


def booking_delete(request):
    return render(request, 'bookings/booking-delete.html')


