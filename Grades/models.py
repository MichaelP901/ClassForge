from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class Grade(models.Model):
    grade_gpa = models.FloatField(null=True, blank=True)
    grade_letter = models.CharField(max_length=2, null=True, blank=True)
    grade_number = models.FloatField(null=True, blank=True)

class ClassAttributes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    course_number = models.CharField(max_length=16, null=True, blank=True)
    requirement = models.CharField(max_length=64)
    class_grade = models.OneToOneField(Grade, on_delete=models.CASCADE, null=True, blank=True)

    
class Assignment(models.Model):
    class_attributes = models.ForeignKey(ClassAttributes, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    assignment_grade = models.OneToOneField(Grade, on_delete=models.CASCADE, null=True, blank=True)


class Exam(models.Model):
    name = models.CharField(max_length=64)
    class_grade = models.OneToOneField(Grade, on_delete=models.CASCADE, null=True, blank=True)

