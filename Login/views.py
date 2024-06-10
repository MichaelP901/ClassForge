from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("HomeScreen:home"))
        else:
             return render(request, "Login/Login.html", {
                  "message": "Invlaid username or password."
             })
    
    return render(request, "Login/Login.html")

def logout_view(request):
     logout(request)
     messages.info(request, "Logged Out")
     return redirect('Login:login_view')

def signup(request):
    
     if request.method == "POST":
          firstname = request.POST["firstname"]
          lastname = request.POST["lastname"]
          email = request.POST["email"]
          password = request.POST["password"]
          password2 = request.POST["re-password"]

          if password == password2:
               if User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Used")
                    return redirect(request.path)
               else:
                    user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname)
                    user.save();
                    return redirect(reverse("Login:login_view"))
          else:
               messages.info(request, "Password Not The Same")
               return redirect(request.path)
     
     else:     
          return render(request, "Login/SignUp.html") 