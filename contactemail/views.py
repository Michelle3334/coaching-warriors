from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Enquiry"
            body = {
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address']
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'coachingwar@gmail.com', [
                    'coachingwar@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, "contact.html", {'form': form})
