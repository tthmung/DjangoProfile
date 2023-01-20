from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home(request):
    return render(request, "home.html")

@cache_page(60 * 15)
def project(request):
    post = ProjectList.objects.all().order_by('-date')
    return render(request, "project.html", {"post": post})
