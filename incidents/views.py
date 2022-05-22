from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import  login, authenticate, logout
from django.contrib.auth.models import User

from .models import Incident
from django.contrib import messages

# Create your views here.

def index(request):
   

    return render(request, 'index.html')

def incident(request):
    if request.method == "POST":
       location1 = request.POST.get('location1')
       description = request.POST.get('description')
       date = request.POST.get('date')
       time = request.POST.get('time')
       location2 = request.POST.get('location2')
       severity = request.POST.get('severity')
       cause = request.POST.get('cause')
       actions = request.POST.get('action')
       type_env = request.POST.get('type_env')
       type_inju = request.POST.get('type_inju')
       type_property = request.POST.get('type_property')
       type_vehicle = request.POST.get('type_vehicle')
       reported_by = request.POST.get('reported_by')
       

       incident = Incident(location1=location1, location2=location2, description=description, date=date,
        time=time, severity=severity, cause=cause, actions=actions, type_env=type_env, type_inju=type_inju,
         type_property=type_property, type_vehicle=type_vehicle, reported_by=reported_by,)
       incident.save()
         
       messages.success(request, 'Your incident has been reported') 
       return redirect("/")

    return render(request, 'incidents.html')

  

def register(request):
    if request.method == "POST":
       username = request.POST.get('username')
       email = request.POST.get('email')
       
       password = request.POST.get('password')

       myuser= User.objects.create_user(username,email,password)
       

       myuser.save()



    return render(request, 'register.html')

def loginUser(request):
       if request.method=="POST":
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
          
          login(request, user)  
          messages.success(request, "Your are logged in!")
          return redirect("/")
          

        else:
            messages.success(request, "Invalid Credentials")
            return render(request, 'login.html')

       return render(request, 'login.html')

def logoutUser(request):
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect("/")       