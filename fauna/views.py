from django.shortcuts import render
from django.http import HttpResponse
from .models import Creature

def all_fauna(request):
    creatures = Creature.objects.all()
    return render(request, 'fauna/all_fauna.html', {'creatures':creatures})
