from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms

# Create your views here.

def userForm(request):
    form = forms.newUserForm()

    if request.method == "POST":
        form = forms.newUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    return render(request, "AppTwo/help.html", {"form":form})


def index(request):
    return render (request, 'AppTwo/index.html')
