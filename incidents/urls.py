from django.contrib import admin
from django.urls import path, include
from incidents import views

urlpatterns = [
    
    path("",views.index, name='index'),
    path("incidents/",views.incident, name='incident'),
    path("login/",views.loginUser, name='loginUser'),
    path("register/",views.register, name='register'),
    path("logout/",views.logoutUser, name='logoutUser'),
    
]