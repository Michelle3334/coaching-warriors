"""Views for Member profile view"""
# from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# from coaches.models import Coach
# from course.models import Course
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

    def get_queryset(self):
        user = self.request.user
        booking_list = Booking.objects.filter(user=user)
        return booking_list


class EditBooking(UpdateView):
    """Edit booking view"""
    model = Booking
    template_name = 'edit_booking.html'
    fields = ['booking_date', 'course_name', 'coach_name']


class DeleteBooking(DeleteView):
    """Delete booking"""
    model = Booking
    template_name = 'delete_booking.html'
    success_message = 'Booking deleted successfully!'
    success_url = reverse_lazy('member_booking')