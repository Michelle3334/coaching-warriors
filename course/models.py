from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Module(models.Model):
    module_name = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.module_name


class Course(models.Model):
    course_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    attendees = models.ManyToManyField(
        User, related_name='course_attendees', blank=True)
    module_name = models.ForeignKey(
        Module, models.SET_NULL, blank=True, null=True, related_name='modules')
    min_people = models.IntegerField(default=0)
    max_people = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.course_name

    def number_of_attendees(self):
        return self.attendees.count()


class Lesson(models.Model):
    module_name = models.ForeignKey(
        Module, models.SET_NULL, blank=True, null=True, related_name='lessons')
    lesson_name = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_name
