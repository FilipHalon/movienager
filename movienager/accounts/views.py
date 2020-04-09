from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views import generic

import accounts.forms as forms


# Create your views here.
def index(request):
    return render(request, "base.html")


class SignUpView(generic.CreateView):
    form_class = forms.UserRegistrationForm
    template_name = 'sign-up.html'
    success_url = 'login'


class SignInView(LoginView):
    template_name = 'sign-in.html'


class UserLogoutView(LogoutView):
    next_page = '/'
