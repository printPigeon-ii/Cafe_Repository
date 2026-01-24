from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import viewsets
import unittest

def index(request):
    return render(request, "main.html")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("main")

    return render(request, "register.html", {"form": form})


class Test(unittest.TestCase):
    def register(request):
        form = UserCreationForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("/cafe/main/")
        return render(request, "register.html", {"form": form})

if __name__ == "__main__":
    unittest.main()

from django.shortcuts import render

def menu(request):
    return render(request, "menu.html")

# Create your views here.
