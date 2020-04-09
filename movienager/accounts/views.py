from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

import accounts.forms as forms
from accounts.models import User


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


class UserManagementView(generic.ListView):
    model = User
    context_object_name = "users"
    template_name = 'user-management.html'
    extra_context = {"form": forms.UserEditForm}

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST.get("email"))
        if len(user) == 1:
            form = forms.UserEditForm(request.POST)
            print(form)
            if form.is_valid():
                user.update(**form.cleaned_data)
                return redirect(reverse("user_management"))
        return redirect(reverse("user_management"))
