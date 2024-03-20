from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")

def result(request, slug):
    return render(request, "result.html")

def signup(request):
    return render(request, "signup.html")

def signout(request):
    return render("index")

def signin(request):
    return render(request, "signin.html")

def detail(request):
    return render(request, "detail.html")
