"""Views for Member profile view"""
# from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ProfileForm, PasswordEditForm
from .models import Booking


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    """View for changing password"""
    form_class = PasswordEditForm
    success_message = 'Password changed successfully!'
    success_url = reverse_lazy('home')


class MemberViewProfile(generic.UpdateView):
    """View and update user profile"""
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user


class BookingView(generic.ListView):
    """Booking list view"""
    model = Booking
    template_name = 'member_booking.html'
