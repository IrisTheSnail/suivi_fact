from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.home, name="first-interface-home"),
    path('bo/', views.bo, name='--bo'),
    path('dcf/', views.dcf, name='--dcf'),
    path('st/', views.st, name='--st'),
]

admin.site.site_header  =  "R.A.D.E.E.F."  
admin.site.site_title  =  "Custom bookstore admin site"
admin.site.index_title  =  "Portail admin de gestion de factures"
