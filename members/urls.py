"""URL paths for members app"""
from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordsChangeView


urlpatterns = [
    path('members/', views.MemberViewProfile.as_view(), name='members'),
    path('password/', PasswordsChangeView.as_view(
        template_name='change_password.html')),
    path('password_success/', views.password_success, name='password_success'),
]
