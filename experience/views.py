from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def experience(request):
    items = experienceList.objects.all().order_by('-date')
    return render(request, "work.html", {"items": items})
