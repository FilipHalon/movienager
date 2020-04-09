from django.urls import path

import accounts.views as views

urlpatterns = [
    path("", views.index),
    path("signup", views.SignUpView.as_view()),
    path("signin", views.SignInView.as_view()),
    path("logout", views.UserLogoutView.as_view()),
    path("user_management", views.UserManagementView.as_view(), name="user_management"),
]
