from django.shortcuts import render
from django.http import JsonResponse
import json
from . import funcs

def inicio(request):  
    return render(request, 'reciclaje/index.html')

def puntoslimpios(request):
    try:
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

from django.shortcuts import render

def mapa(request):
    return render(request, 'reciclaje/mapa.html')

def register(request):
    return render(request, 'reciclaje/register.html')