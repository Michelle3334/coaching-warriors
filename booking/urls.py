"""URL path for booking app"""
from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
]
