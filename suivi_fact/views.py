from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request) :
    return render(request, 'suivi_fact/home.html')

def bo(request) : 
        return render(request, 'suivi_fact/bo.html')