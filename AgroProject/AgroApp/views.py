from django.shortcuts import render,redirect
from .models import User

def index(request):
    return render(request, "index.html",{})


def razdel(request):
    return render(request,"razdel.html",{})


def advert(request):
    return render(request,"advert.html",{})


def form(request):
    return render(request,"form.html",{})


def add(request):
    return render(request,"add.html",{})

def regist(request):
    if request.POST:
        baza = User()
        baza.UserNameOne = request.POST.get("user_type")
        baza.UserNameTwo = request.POST.get("NameOne")
        baza.UserEmail = request.POST.get("NameTwo")
        baza.UserPassword = request.POST.get("NameSri")
        baza.UserPhone =request.POST.get("NameFoo")
        if request.POST.get("agree") == "Yes":
            baza.UserOferta = True
        else:
            baza.UserOferta = False
        baza.save()
        return redirect("index")
    ctx={}

    return render(request,"registratsiya.html",ctx)