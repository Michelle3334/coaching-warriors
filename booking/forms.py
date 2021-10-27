from django import forms
from phonenumber_field.formfields import PhoneNumberField


class BookingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = PhoneNumberField(widget=forms.TextInput(), required=True)
    course = forms.CharField()
    coach = forms.CharField()
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    additional_information = forms.CharField(
        widget=forms.Textarea, required=False)
