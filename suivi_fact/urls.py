from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="first-interface-home"),
    path('bo/', views.bo, name='--bo'),
    path('dcf/', views.dcf, name='--dcf'),
    path('st/', views.st, name='--st'),
]
