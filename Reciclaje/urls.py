from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('puntoslimpios', views.puntoslimpios, name='puntoslimpios')
]
