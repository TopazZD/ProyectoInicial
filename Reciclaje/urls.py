from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  
    path('mapa/', views.mapa, name='mapa'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='reciclaje/registro/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('info_reciclaje', views.info_reciclaje, name='info_reciclaje'),
    path('puntoslimpios', views.puntoslimpios, name='puntoslimpios'),
    path('api/materiales/', views.como_reciclar, name='api_materiales'),
]
