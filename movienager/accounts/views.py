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

    @staticmethod
    def render_if_form_error(request, error_message):
        context = {"form": forms.UserEditForm, "users": User.objects.all(), "error": error_message}
        return render(request, 'user-management.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.POST.get("email"))
        if len(user) == 1:
            if "delete" in request.POST:
                user.delete()
            username=request.POST.get("username")
            if user.filter(username=username) or len(User.objects.filter(username=username)) == 0:
                form = forms.UserEditForm(request.POST)
                print(form)
                if form.is_valid():
                    password = form.cleaned_data.pop('password')
                    if password:
                        user.set_password(password)
                    user.update(**form.cleaned_data)
                    return redirect("user_management")
                return self.render_if_form_error(request, "The provided data was not correct.")
            return self.render_if_form_error(request, "A user with this username already exists.")
        return self.render_if_form_error(request, "Changing an e-mail is not allowed.")
