"""Views for coaches app"""
from django.views import generic
from .models import Coach


class CoachList(generic.ListView):
    """Coach list view"""
    model = Coach
    queryset = Coach.objects.filter(status=1)
    template_name = 'about.html'
