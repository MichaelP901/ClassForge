from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

@login_required(login_url='Login:login_view')
def links(request):
    return render(request, "discounts/Links.html")