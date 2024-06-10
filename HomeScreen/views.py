from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from Grades.models import *

# Create your views here.

@login_required(login_url='Login:login_view')
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("Login:login_view"))
    
    assignments = Assignment.objects.filter(
        class_attributes__user = request.user
    )

    return render(request, "HomeScreen/home.html", {
        "assignments": assignments
    })
