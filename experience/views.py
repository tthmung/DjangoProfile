from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def experience(request):
    items = experienceList.objects.all().order_by('-date')
    return render(request, "work.html", {"items": items})
