from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'home.html', {"first_name": "Stephen"})


def search(request):
    return HttpResponse("Welcome to the search page!")


def admin(request):
    return HttpResponse("Welcome to the admin page!")
