from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    navBarOptions = {
        "Home": {"status": "active", "url": "index"},
        "Search": {"status": "", "url": "search"},
        "Admin": {"status": "", "url": "admin"}
    }
    return render(request, 'home.html', {"first_name": "Stephen", "navbarOptions": navBarOptions})


def search(request):
    return HttpResponse("Welcome to the search page!")


def administration(request):
    return HttpResponse("Welcome to the admin page!")
