from django.urls import path, include
from booking_website.booking_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', include([
        path('register/', views.profile_register, name='profile-register'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete'),
        path('details/', views.profile_details, name='profile-details')
    ])),
    path('apartment/', include([
        path('details/', views.apartment_details, name='apartment-details'),
        path('catalogue/', views.apartment_catalogue, name='apartment-catalogue'),
        path('book/', views.apartment_book, name='apartment-book')
    ])),
    path('booking/', include([
        path('', views.my_bookings, name='my-bookings'),
        path('<int:pk>/details/', views.my_bookings, name='booking-details'),
        path('<int:pk>/edit/', views.booking_edit, name='booking-edit'),
        path('<int:pk>/delete/', views.booking_delete, name='booking-delete')
    ]))
]