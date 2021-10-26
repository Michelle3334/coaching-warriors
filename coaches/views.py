from django.views import generic
from .models import Coach


class CoachList(generic.ListView):
    model = Coach
    queryset = Coach.objects.filter(status=1)
    template_name = 'about.html'
