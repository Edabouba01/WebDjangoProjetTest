from rest_framework import routers
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
     
]
