from django.contrib.auth import views as auth_views 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mapa/', views.mapa, name='mapa'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('puntoslimpios/', views.puntoslimpios, name='puntoslimpios'),
]
