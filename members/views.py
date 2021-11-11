"""Views for Member profile view"""
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from .forms import ProfileForm
from django.contrib import messages
# from django.urls import reverse_lazy


class MemberViewProfile(generic.UpdateView):
    """View and update user profile"""
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user
