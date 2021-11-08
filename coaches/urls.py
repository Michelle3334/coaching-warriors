"""URL path for coaches app"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.CoachList.as_view(), name='about'),
]
