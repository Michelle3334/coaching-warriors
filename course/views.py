"""Views for course app"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Course


class CourseList(generic.ListView):
    """Course list view"""
    model = Course
    queryset = Course.objects.filter(status=1)
    template_name = 'index.html'


class CourseDetail(View):
    """Course detail view"""
    def get(self, request, slug):
        """Return render view for course detail"""
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
            }
        )


class Gallery(TemplateView):
    """Gallery view"""
    template_name = 'gallery.html'

    def gallery(self, request):
        """Return render view for gallery"""
        return render(request, 'gallery.html')


class About(TemplateView):
    """About us page view"""
    template_name = 'about.html'

    def about(self, request):
        """Return render view for about page"""
        return render(request, 'about.html')
