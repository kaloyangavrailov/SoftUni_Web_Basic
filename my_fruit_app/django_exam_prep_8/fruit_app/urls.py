from django.urls import path, include
from django_exam_prep_8.fruit_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fruit/', include([
        path('create/', views.fruit_create, name='fruit-create'),
        path('<int:pk>/details/', views.fruit_details, name='fruit-details'),
        path('<int:pk>/edit/', views.fruit_edit, name='fruit-edit'),
        path('<int:pk>/delete/', views.fruit_delete, name='fruit-delete'),
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile-create'),
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete')
    ]))
]