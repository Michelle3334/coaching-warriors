from django.shortcuts import render
from django.views import generic
from .models import Coach


class Coaches(generic.ListView):
    model = Coach
    queryset = Coach.objects.filter(status=1)
    template_name = 'about.html'
