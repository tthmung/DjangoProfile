from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def project(request):
    post = ProjectList.objects.all().order_by('-date')
    return render(request, "project.html", {"post": post})

def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")

def termofservice(request):
    return render(request, "termofservice.html")

def privacy(request):
    return render(request, "privacy.html")
