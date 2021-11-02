"""Application configuration for booking app"""
from django.apps import AppConfig


class BookingConfig(AppConfig):
    """Booking configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
