from . import views
from django.urls import path


urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('gallery/', views.Gallery.as_view(), name='gallery'),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),
]
