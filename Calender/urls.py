
from django.urls import path

from . import views

app_name = 'Calender'

urlpatterns = [
    path("", views.calender, name="calender")
]
