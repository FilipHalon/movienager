from django.urls import path

import accounts.views as views

urlpatterns = [
    path("signup", views.SignUp.as_view()),
]
