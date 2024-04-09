from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello, world.")


def about(request):
    return HttpResponse("<strong>About</strong>")


def index(request):
    context = {
        "teacher": {"name": "John", "lastname": "Doe", "age": 25},
    }
    return render(request, "Centre/index.html", context)
