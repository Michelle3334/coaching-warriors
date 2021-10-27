from django import forms


class BookingForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_address = forms.EmailField(required=True)
    telephone = forms.IntegerField(required=True)
    course = forms.CharField()
    coach = forms.CharField()
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))                   
    additional_information = forms.CharField(
        widget=forms.Textarea, required=False)
