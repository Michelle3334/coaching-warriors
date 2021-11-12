"""Forms for Members"""
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
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
        """Meta class"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            )


class PasswordEditForm(PasswordChangeForm):
    """Password change view"""
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password'}))

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'old_password',
            'new_password1',
            'new_password1',
            )
