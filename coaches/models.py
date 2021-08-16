from django.db import models
from cloudinary.models import CloudinaryField


STATUS = ((0, "Inactive"), (1, "Active"))


class Coach(models.Model):
    coach_name = models.CharField(
        primary_key=True, max_length=200, unique=True)
    email = models.EmailField()
    profile_image = CloudinaryField('image', default='placeholder')
    title = models.CharField(max_length=100)
    about = models.TextField()

    class Meta:
        ordering = ['coach_name']

    def __str__(self):
        return self.coach_name
