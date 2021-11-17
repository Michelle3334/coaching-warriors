"""Application configuration for Members app"""
from django.apps import AppConfig


class MembersConfig(AppConfig):
    """Members app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'members'
