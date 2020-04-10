from django.urls import path, re_path

import accounts.views as views

urlpatterns = [
    path("", views.index),
    path("signup", views.SignUpView.as_view()),
    path("signin", views.SignInView.as_view()),
    path("logout", views.UserLogoutView.as_view()),
    path("user_management", views.UserManagementView.as_view(), name="user_management"),
    path("user_list", views.UserListView.as_view()),
    re_path(r"^user_edit/(?P<pk>[\w@\.]+$)", views.UserEditView.as_view(), name="user-edit"),
    re_path(r"^user_delete/(?P<pk>[\w@\.]+$)", views.UserDeleteView.as_view(), name="user-delete")
]
