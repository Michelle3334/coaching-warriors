"""URL paths for members app"""
from django.urls import path
from . import views
from .views import PasswordsChangeView


urlpatterns = [
    # path('members/', views.BookingView.as_view(), name='booking'),
    path('members/', views.MemberViewProfile.as_view(), name='members'),
    path('password/', PasswordsChangeView.as_view(
        template_name='change_password.html')),
]
