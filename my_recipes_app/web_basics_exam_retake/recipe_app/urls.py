from django.urls import path, include
from web_basics_exam_retake.recipe_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', include([
        path('catalogue/', views.recipe_catalogue, name='recipe-catalogue'),
        path('create/', views.recipe_create, name='recipe-create'),
        path('<int:pk>/details/', views.recipe_details, name='recipe-details'),
        path('<int:pk>/edit/', views.recipe_edit, name='recipe-edit'),
        path('<int:pk>/delete/', views.recipe_delete, name='recipe-delete')
    ])),
    path('profile/', include([
        path('create/', views.profile_create, name='profile-create'),
        path('details/', views.profile_details, name='profile-details'),
        path('edit/', views.profile_edit, name='profile-edit'),
        path('delete/', views.profile_delete, name='profile-delete')
    ]))
]