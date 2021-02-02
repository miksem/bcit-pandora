from django.shortcuts import render

from django.http import HttpResponse
from .models import Landscape

def all_geography(request):
    landscapes = Landscape.objects.all()
    return render(request, 'geography/all_geography.html', {'landscapes':landscapes})
