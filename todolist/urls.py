from django.urls import path
from todolist.views import show_todolist, login_user, logout_user, register

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name = "show_todolist"),
    path("login/", login_user, name = "login_user"),
    path("logout/", logout_user, name = "logout_user"),
    path("register/", register, name = "register"),
]