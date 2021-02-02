from django.shortcuts import render

from django.http import HttpResponse
from .models import Plant

def all_flora(request):
    plants = Plant.objects.all()
    return render(request, 'flora/all_flora.html', {'plants':plants})
