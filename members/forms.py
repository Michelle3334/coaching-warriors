"""Forms for Members"""
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm, LoginForm, ChangePasswordForm
from .models import Booking


class UserRegisterForm(SignupForm):
    """Registration form"""
    class Meta:
        """Meta class"""
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserLoginForm(LoginForm):
    """Login form"""
    class Meta:
        """Meta class"""
        model = User
        fields = ('login', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'


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
            )


class PasswordEditForm(ChangePasswordForm):
    """Password change view"""
    oldpassword = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'type': 'password'}))
    password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password'}))
    password2 = forms.CharField(
        label="New password (again)",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 'type': 'password'}))

    class Meta:
        """Meta class"""
        model = User
        fields = (
            'oldpassword',
            'password1',
            'password1',
            )


class CreateBookingForm(forms.ModelForm):
    """Create new booking form"""
    booking_date = forms.DateField(
        widget=forms.TextInput(attrs={
            'type': 'date', 'class': 'form-control'}))
    # course_name = forms.CharField(
    #    widget=forms.Select(attrs={'class': 'form-control'}))
    # coach_name = forms.CharField(
    #    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        """Meta class"""
        model = User
        model = Booking
        fields = (
            'booking_date',
            'course_name',
            'coach_name',
            )
