from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Booking(TemplateView):
    template_name = 'booking.html'

    def booking(self, request):
        return render(request, 'booking.html')
