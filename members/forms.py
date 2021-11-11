"""Form for User Profile"""
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms


class ProfileForm(UserChangeForm):
    """View and edit profile"""
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            )
