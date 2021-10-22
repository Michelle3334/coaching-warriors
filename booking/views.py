from django.views.generic import TemplateView
from django.shortcuts import render
from course.models import Course


class Booking(TemplateView):
    template_name = 'booking.html'
    course_list = Course.objects.filter(status=1)

    def booking(self, request):
        return render(request, 'booking.html', {'course_list': course_list})
