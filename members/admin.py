"""Display model in Django Admin panel"""
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Booking Fields for display and filter"""
    list_display = ('user', 'booking_date', 'course_name', 'coach_name')
    search_fields = ['booking_date', 'user', 'course_name', 'coach_name']
    list_filter = ('booking_date', 'user')
