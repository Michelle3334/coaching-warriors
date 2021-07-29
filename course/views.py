from django.shortcuts import render
from django.views import generic
from .models import Course


class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 3
