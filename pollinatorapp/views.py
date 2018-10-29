from django.shortcuts import render
import csv, io

# Create your views here.
# from pollinatorapp.models import Pollinator


def home(request):
    return render(request, 'pages/home.html', {})


def maps(request):
    return render(request, 'pages/maps-google-maps.html', {})


