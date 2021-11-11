"""URL paths for members app"""
from django.urls import path
from .views import MemberRegisterView


urlpatterns = [
    path('signup/', MemberRegisterView.as_view(), name='signup'),
]
