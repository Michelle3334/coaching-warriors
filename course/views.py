from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
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
        module = course.module.order_by('created_on')
        lesson = module.lesson.order_by('created_on')

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "module": module,
                "lesson": lesson,
            }
        )
