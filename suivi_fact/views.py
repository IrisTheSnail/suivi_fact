from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request) :
    return HttpResponse('<h1>first interface Home</h1>')

def about(request) : 
    return HttpResponse('<h1>ha page khora, f9lb home</h1>')