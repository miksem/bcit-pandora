from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_vendors, name='all_vendors'),
]
