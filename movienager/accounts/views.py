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


class UserListView(generic.ListView):
    model = User
    context_object_name = "users"
    template_name = 'user-list.html'


class UserEditView(generic.UpdateView):
    model = User
    template_name = 'user-edit.html'
    success_url = '/user_list'
    form_class = forms.UserExtendedEditForm


class UserDeleteView(generic.DeleteView):
    model = User
    template_name = 'user-delete.html'
    success_url = '/user_list'


class UserManagementView(generic.ListView):
    model = User
    context_object_name = "users"
    template_name = 'user-management.html'
    extra_context = {"form": forms.UserEditForm, "choices": User.TYPES}

    def render_if_form_error(self, request, error_message):
        context = {"users": User.objects.all(), "error": error_message}
        context.update(self.extra_context)
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
                    print(form.cleaned_data)
                    password = form.cleaned_data.pop('password')
                    if password:
                        user[0].set_password(password)
                        user[0].save()
                    user.update(**form.cleaned_data)
                    return redirect("user_management")
                return self.render_if_form_error(request, "The provided data was not correct.")
            return self.render_if_form_error(request, "A user with this username already exists.")
        return self.render_if_form_error(request, "Changing an e-mail is not allowed.")
