"""Views for Member profile view"""
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from allauth.account.views import PasswordChangeView
# from coaches.models import Coach
# from course.models import Course
from .forms import UserRegisterForm, UserLoginForm, ProfileForm, PasswordEditForm, CreateBookingForm
from .models import Booking


class UserRegisterView(generic.CreateView):
    """User Registration form"""
    form_class = UserRegisterForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('home')

    def save(self, request):
        """Save user to user model"""
        user = super(UserRegisterForm. self).save(request)
        return user


class UserLoginView(generic.CreateView):
    """User login view"""
    form_class = UserLoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')

    def login(self, *args, **kwargs):
        """User login return"""
        return super(UserLoginForm, self).login(*args, **kwargs)


class PasswordsChangeView(PasswordChangeView):
    """View for changing password"""
    form_class = PasswordEditForm
    success_message = 'Password changed successfully!'
    success_url = reverse_lazy('members')

    def save(self):
        """Save new password to model"""
        super(PasswordEditForm, self).save()


class MemberViewProfile(generic.UpdateView):
    """View and update user profile"""
    form_class = ProfileForm
    template_name = 'profile.html'
    success_message = 'Profile updated successfully!'
    success_url = reverse_lazy('members')

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


class CreateBookingView(CreateView):
    """Create new booking view"""
    model = Booking
    form_class = CreateBookingForm
    template_name = 'create_booking.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateBookingView, self).form_valid(form)


class EditBooking(UpdateView):
    """Edit booking view"""
    model = Booking
    form_class = CreateBookingForm
    template_name = 'edit_booking.html'


class DeleteBooking(DeleteView):
    """Delete booking"""
    model = Booking
    template_name = 'delete_booking.html'
    success_message = 'Booking deleted successfully!'
    success_url = reverse_lazy('member_booking')
