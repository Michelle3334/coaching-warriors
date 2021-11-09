"""Form for User Profile"""
from django import forms


class ProfileForm(forms.Form):
    """View profile form fields"""
    username = forms.CharField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField(required=True)
