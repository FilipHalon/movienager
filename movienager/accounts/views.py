import json

from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic

import accounts.forms as forms
from accounts.models import User


# Create your views here.
def index(request):
    return render(request, "index.html")


def admin_panel(request):
    return redirect("admin-panel-user-mng")


class SignUpView(generic.CreateView):
    form_class = forms.UserRegistrationForm
    template_name = "auth_forms/signup.html"
    success_url = "signin"


class SignInView(LoginView):
    template_name = "auth_forms/signin.html"
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = "/"


class AddUserRequired(PermissionRequiredMixin):
    login_url = "signin"
    permission_required = "accounts.add_user"


class AdminPanelUserMngView(AddUserRequired, generic.ListView):
    model = User
    context_object_name = "users"
    template_name = "user_management/admin-panel-user-mng.html"


class UserEditView(AddUserRequired, generic.UpdateView):
    model = User
    template_name = "user_forms/user-edit.html"
    success_url = "/admin_panel/user_management"
    form_class = forms.UserExtendedEditForm


class UserDeleteView(AddUserRequired, generic.DeleteView):
    model = User
    template_name = "user_forms/user-delete.html"
    success_url = "/admin_panel/user_management"


class UserManagementView(AddUserRequired, generic.ListView):
    model = User
    context_object_name = "users"
    template_name = "user_management/user-management.html"
    extra_context = {"form": forms.UserEditForm, "choices": User.TYPES}

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.POST.get("email"))
        except MultipleObjectsReturned:
            return HttpResponse("You cannot change the e-mail.")

        form = forms.UserEditForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.set_permission()
        return HttpResponse("Edited")
