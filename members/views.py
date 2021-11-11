"""Views for Member profile view"""
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm


class RegisterView(View):
    """View for sign up form"""
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        """Get request"""
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """Post request"""
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
