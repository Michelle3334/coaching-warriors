"""URL paths for members app"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('members/', views.MemberViewProfile.as_view(), name='members'),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='change_password.html')),
]
