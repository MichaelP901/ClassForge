from django.urls import path
from . import views

app_name  = 'Grades'

urlpatterns = [
    path("", views.grades, name="grades"),
    path("addclass", views.classAdd, name="classAdd"),
    path("deleteclass", views.classDelete, name="classDelete"),
    path("<str:course_number>/", views.getAssignments, name="getAssignments"),
    path("addAssignment", views.assignmentAdd, name="assignmentAdd"),
    path("deleteAssignment", views.assignmentDelete, name="assignmentDelete"),
]
