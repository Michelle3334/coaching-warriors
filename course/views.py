from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Course


class CourseList(generic.ListView):
    model = Course
    queryset = Course.objects.filter(status=1)
    template_name = 'index.html'
    paginate_by = 6


class CourseDetail(View):

    def get(self, request, slug, *args, **kwargs):
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
    template_name = 'gallery.html'

    def gallery(self, request):
        return render(request, 'gallery.html')


class About(TemplateView):
    template_name = 'about.html'

    def about(self, request):
        return render(request, 'about.html')


class Contact(TemplateView):
    template_name = 'contact.html'

    def contact(self, request):
        return render(request, 'contact.html')
