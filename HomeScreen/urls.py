from django.urls import path
from . import views

app_name = 'HomeScreen'

urlpatterns = [
    path("", views.home, name = "home")
]