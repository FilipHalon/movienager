from django.shortcuts import render
from django.views import generic

import accounts.forms as forms


# Create your views here.
class SignUp(generic.CreateView):
    form_class = forms.UserRegistrationForm
    template_name = 'sign-up.html'
    success_url = 'login'
