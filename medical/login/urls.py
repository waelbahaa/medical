from django.contrib import admin
from django.urls import path,include
from login import views
urlpatterns = [
    path('', views.login_info,name="register"),
    
]