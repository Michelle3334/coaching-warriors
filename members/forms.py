"""Form for User Profile"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """Customised registration fields"""
    first_name = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', }))
    last_name = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', }))
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', }))
    email = forms.EmailField(
        required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', }))
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
                }))
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'data-toggle': 'password',
                'id': 'password',
                }))

    class Meta:
        """Meta class"""
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
            ]
