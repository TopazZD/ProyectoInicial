import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

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
            user = form.save()
            login(request, user)
            return redirect('mapa')
    else:
        form = RegistroForm()
    return render(request, 'reciclaje/registro.html', {'form': form})


@login_required
def mapa(request):
    comuna = ''
    if hasattr(request.user, 'perfil'):
        comuna = request.user.perfil.comuna
    return render(request, 'reciclaje/mapa.html', {
        'comuna': comuna,
        'comunas': obtener_comunas(),
    })


def puntoslimpios(request):
    try:
        with open(RUTA_GEO, "r", encoding="UTF-8") as f:
            data = json.load(f)

        comuna = request.GET.get("comuna")
        if comuna:
            data = [
                p for p in data
                if p.get("commune") and p["commune"].get("name", "").strip().lower() == comuna.strip().lower()
            ]

        # filtros posibles: glass paper paperboard cardboard_drink plastic metal power_bank phone
        filter: list = request.GET.getlist("filter")

        lat = request.GET.get("lat")
        long = request.GET.get("long")
        dist = request.GET.get("dist")
        if lat and long and dist:
            data = funcs.geo_filter(data, float(lat), float(long), float(dist), filter)
        elif filter:
            data = [p for p in data if all(m in p.get("materials", []) for m in filter)]

        return JsonResponse(data, safe=False)
    except Exception:
        return JsonResponse({"Error": "No se han podido obtener resultados con los datos dados"})