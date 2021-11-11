"""URL paths for members app"""
from django.urls import path
from .views import RegisterView


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
]
