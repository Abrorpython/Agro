from django.shortcuts import render, redirect
from .models import User, Province, Region,Categoriya,Obyavleniya,News,Sostayanie
from .models import User, Province,ChastnoLitso,Nalichie,Edinitsva
from .forms import NewsForm
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, "index.html", {})


def razdel(request):
    return render(request, "razdel.html", {})


def advert(request):
    return render(request, "advert.html", {})


def form(request,):
    provines = Province.objects.all()
    category = Categoriya.objects.all()
    obyavleniya = Obyavleniya.objects.all()
    sostayanie = Sostayanie.objects.all()
    chastnolitso = ChastnoLitso.objects.all()
    nalichie = Nalichie.objects.all()
    edinitstva = Edinitsva.objects.all()
    if request.POST and request.FILES:
        form = NewsForm(request.POST,request.FILES)
        rasmlar = request.FILES.getlist("rasmlar", [])
        images = []
        for rasm in rasmlar:
            fs = FileSystemStorage()
            filename = fs.save(rasm.name, rasm)
            uploaded_file_url = fs.url(filename)
            images.append(uploaded_file_url)
        if form.is_valid():
            form.save(images=images)


    ctx = {
        "provines": provines,
        "category": category,
        "obyavleniya":obyavleniya,
        "sostayanie":sostayanie,
        "chastnolitso":chastnolitso,
        "nalichie":nalichie,
        "edinitstva":edinitstva,

    }
    return render(request, "form.html", ctx)


def add(request):
    return render(request, "add.html", {})


def regist(request):
    if request.POST:
        baza = User()
        baza.UserNameOne = request.POST.get("user_type")
        baza.UserNameTwo = request.POST.get("NameOne")
        baza.UserEmail = request.POST.get("NameTwo")
        baza.UserPassword = request.POST.get("NameSri")
        baza.UserPhone = request.POST.get("NameFoo")
        if request.POST.get("agree") == "Yes":
            baza.UserOferta = True
        else:
            baza.UserOferta = False
        baza.save()
        return redirect("index")
    ctx = {}

    return render(request, "registratsiya.html", ctx)


def customers(request):
    ctx={}
    return render(request,'customers.html',ctx)


def salers(request):
    ctx={}
    return render(request,'salers.html',ctx)

