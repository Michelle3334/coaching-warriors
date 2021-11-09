from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
# from .forms import ProfileForm


# class MemberViewProfile(generic.CreateView):
    # form = ProfileForm
#    template_name = 'profile.html'
#    success_url = reverse_lazy('profile')

class MemberViewProfile(TemplateView):
    """Member profile page view"""
    template_name = 'profile.html'

    def about(self, request):
        """Return render view for member view profile page"""
        return render(request, 'profile.html')
