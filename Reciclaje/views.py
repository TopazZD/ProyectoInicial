from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
import json
from . import funcs
from .comunas import obtener_comunas, RUTA_GEO
from .forms import RegistroForm

def inicio(request):  
    if request.user.is_authenticated:
        return redirect('mapa')
    return render(request, 'reciclaje/inicio.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('mapa')
    else:
        form = RegistroForm()
    return render(request, 'reciclaje/register.html', {'form': form})

@login_required
def mapa(request):
    comuna =''
    if hasattr(request.user, 'perfil'):
        comuna = request.user.perfil.comuna
    return render(request, 'reciclaje/mapa.html', {'comuna': comuna, 'comunas': obtener_comunas()})

def puntoslimpios(request):
    try:
<<<<<<< HEAD
        with open(RUTA_GEO, 'r', encoding='utf-8') as f:
            data = json.load(f)
        comuna= request.GET.get('comuna')
        if comuna:
            data = [p for p in data if p.get('comuna') and p['comuna'].get('nombre','').strip().lower() == comuna.strip().lower()]
        filter: list = request.GET.getlist('filter')
        lat = request.GET.get('latitud')
        long = request.GET.get('longitud')
        dist = request.GET.get('dist')
        if lat and long and dist: 
            data = funcs.geo_filter(data, float(lat), float(long), float(dist), filter) 
      
        return JsonResponse(data, safe=False)
    except Exception:
        return JsonResponse({'error': 'Error al procesar la solicitud'}, status=500)
=======
        data = json.load(open("Reciclaje/data/geo.json", "r", encoding="UTF-8"))
        lat = float(request.GET.get("lat"))
        long = float(request.GET.get("long"))
        dist = float(request.GET.get("dist"))
        filter:list = request.GET.getlist("filter")
        
        # filtros posibles: glass paper paperboard cardboard_drink plastic metal power_bank phone

        res = funcs.geo_filter(data, lat, long, dist, filter)

        return JsonResponse(res, safe=False)
    except:
        return JsonResponse({"Error":"No se han podido obtener resultados con los datos dados"})

def mapa(request):
    return render(request, 'reciclaje/mapa.html')

def register(request):
    return render(request, 'reciclaje/register.html')
>>>>>>> 2a1364a7d5ffb4109caedadc26857cedb0c9a7c3
