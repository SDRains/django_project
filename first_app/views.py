from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    names = {"Stephen": "Stephen"}
    return render(request, 'home.html', context=names)


def home(request):
    return HttpResponse("Welcome to the home page!")


def educative(request):
    return HttpResponse("Welcome to the educative page!")
