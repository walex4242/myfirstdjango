from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def wale(request):
    return HttpResponse("Hello, Olawale Motunrayo's Husband")
def motunrayo(request):
    return HttpResponse("Hello, This is Motunrayo")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
})
