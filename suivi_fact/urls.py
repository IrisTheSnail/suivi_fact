from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="first-interface-home"),
    path('about/', views.about, name='--about'),
]