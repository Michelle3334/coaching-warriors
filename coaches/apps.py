"""Application configuration for coaches app"""
from django.apps import AppConfig


class CoachesConfig(AppConfig):
    """Coaches configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coaches'
