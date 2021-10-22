from django.core.mail import send_mail, BadHeaderError
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages


class Booking(TemplateView):
    template_name = 'booking.html'

    def booking(self, request):
        return render(request, 'booking.html')