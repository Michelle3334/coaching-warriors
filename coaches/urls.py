"""URL path for coaches app"""
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.CoachList.as_view(), name='about'),
]
