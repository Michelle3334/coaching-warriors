"""Database models for course app"""
from django.db import models
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Course(models.Model):
    """Model for courses"""
    course_name = models.CharField(
        primary_key=True, max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """Class for ordering"""
        ordering = ['-created_on']

    def __str__(self):
        return str(self.course_name)
