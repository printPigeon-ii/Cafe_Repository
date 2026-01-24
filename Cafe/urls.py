from django.urls import path
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.index, name="main"),
    path("register/", views.register, name="register"),
    path("menu/", views.menu, name="menu"),
]