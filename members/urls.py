"""URL paths for members app"""
from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.MemberViewProfile.as_view(), name='members'),
]
