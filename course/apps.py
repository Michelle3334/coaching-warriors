"""Application configuration for course app"""
from django.apps import AppConfig


class CourseConfig(AppConfig):
    """Course app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course'
