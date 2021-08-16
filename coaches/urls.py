from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.Coaches.as_view(), name='about'),
]
