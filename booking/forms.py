from django import forms
import datetime


class BookingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=12, required=True)
    date = forms.DateField(required=True, initial=datetime.date.today)
    message = forms.CharField(widget=forms.Textarea, required=False)
