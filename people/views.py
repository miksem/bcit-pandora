from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def all_people(request):
    people = Person.objects.all()
    return render(request, 'people/all_people.html', {'people':people})
