from django.urls import path

import accounts.views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin_panel", views.admin_panel, name="admin-panel"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin", views.SignInView.as_view(), name="signin"),
    path("logout", views.UserLogoutView.as_view(), name="logout"),
    path("user_management", views.UserManagementView.as_view(), name="user-management"),
    path(
        "admin_panel/user_management",
        views.AdminPanelUserMngView.as_view(),
        name="admin-panel-user-mng",
    ),
    path(
        "^user_edit/<pk>",
        views.UserEditView.as_view(),
        name="user-edit",
    ),
    path(
        "user_delete/<pk>",
        views.UserDeleteView.as_view(),
        name="user-delete",
    ),
]
