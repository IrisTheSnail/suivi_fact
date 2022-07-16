from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request) :
    return render(request, 'suivi_fact/home.html')

def bo(request) : 
    return render(request, 'suivi_fact/bo.html', {'title': 'bo'})

def dcf(request) : 
    return render(request, 'suivi_fact/dcf.html', {'title': 'dcf'})

def st(request) : 
    return render(request, 'suivi_fact/st.html', {'title': 'st'})