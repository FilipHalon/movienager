from django.urls import path

import accounts.views as views

urlpatterns = [
    path("signup", views.SignUpView.as_view()),
    path("signin", views.SignInView.as_view()),
    path("logout", views.UserLogoutView.as_view()),
]
