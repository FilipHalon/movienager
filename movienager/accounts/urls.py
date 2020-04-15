from django.urls import path, re_path

import accounts.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", views.SignInView.as_view(), name="signin"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("user_management", views.UserManagementView.as_view(), name="user-management"),
    path("admin_panel/user_management", views.AdminPanelUserMngView.as_view(), name="admin-panel-user-mng"),
    re_path(r"^user_edit/(?P<pk>[\w\-@\._]+$)", views.UserEditView.as_view(), name="user-edit"),
    re_path(r"^user_delete/(?P<pk>[\w\-@\._]+$)", views.UserDeleteView.as_view(), name="user-delete")
]
