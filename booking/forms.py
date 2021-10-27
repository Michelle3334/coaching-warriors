from django import forms
from phonenumber_field.formfields import PhoneNumberField
from course.models import Course
from coaches.models import Coach


class BookingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = PhoneNumberField(widget=forms.TextInput(), required=True)
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(status=1), 
        empty_label="(Please select a course)")
    coach = forms.ModelChoiceField(
        queryset=Coach.objects.filter(status=1), 
        empty_label="(Please select a coach)")
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    additional_information = forms.CharField(
        widget=forms.Textarea, required=False)
