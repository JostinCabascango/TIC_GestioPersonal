from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello, world.")


def about(request):
    return render(request, "Centre/about.html", {})


def index(request):
    context = {
        "teacher": {"name": "John", "lastname": "Doe", "age": 25},
    }
    return render(request, "Centre/index.html", context)


def students(request):
    pass


def teacher(request):
    pass
