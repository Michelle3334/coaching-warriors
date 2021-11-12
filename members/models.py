"""Database models for members to book a course"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from coaches.models import Coach
from course.models import Course


class Booking(models.Model):
    """Model for member booking"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.ForeignKey(
        Course, on_delete=models.CASCADE, limit_choices_to={'status': '1'})
    coach_name = models.ForeignKey(
        Coach, on_delete=models.CASCADE, limit_choices_to={'status': '1'})
    booking_date = models.DateField(unique=True)

    class Meta:
        """Class for ordering"""
        ordering = ['booking_date']

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        """URL to return to on edit"""
        return reverse('member_booking')
