"""URL paths for course app"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('about/', views.About.as_view(), name='about'),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),
]
