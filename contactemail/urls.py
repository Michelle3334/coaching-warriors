"""URL path for contactemail app"""
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
