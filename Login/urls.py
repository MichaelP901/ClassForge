from django.urls import path
from . import views

app_name = 'Login'

urlpatterns = [
    path("login_view/", views.login_view, name="login_view"),
    path("signup/", views.signup, name="signup"),
    path("logout_view/", views.logout_view, name="logout_view"),
]