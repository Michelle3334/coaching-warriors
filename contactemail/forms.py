from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email_address = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
