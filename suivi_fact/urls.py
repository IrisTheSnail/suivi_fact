from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="first-interface-home"),
    path('bo/', views.bo, name='--bo'),

]
