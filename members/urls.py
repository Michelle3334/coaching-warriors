"""URL paths for members app"""
from django.urls import path, include
from . import views
from .views import PasswordsChangeView, CreateBookingView, EditBooking, DeleteBooking


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('members/', views.MemberViewProfile.as_view(), name='members'),
    path(
        'member_booking/', views.BookingView.as_view(), name='member_booking'),
    path('password/', PasswordsChangeView.as_view(
        template_name='change_password.html')),
    path(
        'member_booking/edit/<int:pk>',
        EditBooking.as_view(), name="edit_booking"),
    path(
        'member_booking/<int:pk>/delete',
        DeleteBooking.as_view(), name="delete_booking"),
    path(
        'create_booking/',
        CreateBookingView.as_view(), name="create_booking"),
]
