from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='user-profile'),
    path('update/', views.fupdate_profile, name='update-profile'),
]