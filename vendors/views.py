from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor

def all_vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendors/all_vendors.html', {'vendors':vendors})
