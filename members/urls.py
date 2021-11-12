"""URL paths for members app"""
from django.urls import path
from . import views
from .views import PasswordsChangeView


urlpatterns = [
    path('members/', views.MemberViewProfile.as_view(), name='members'),
    path(
        'member_booking/', views.BookingView.as_view(), name='member_booking'),
    path('password/', PasswordsChangeView.as_view(
        template_name='change_password.html')),
]
