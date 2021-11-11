"""Views for Member profile view"""
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import ProfileForm


class PasswordsChangeView(PasswordChangeView):
    """View for changing password"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    """Success message for password change"""
    return render(request, 'password_success.html', {})


class MemberViewProfile(generic.UpdateView):
    """View and update user profile"""
    form_class = ProfileForm
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user
