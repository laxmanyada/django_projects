from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup.html/',views.signup, name='signup'),
    path('login.html/', views.loginn, name='loginn'),
]
