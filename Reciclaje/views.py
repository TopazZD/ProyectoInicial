from django.shortcuts import render


def index(request):
    return render(request,"reciclaje/index.html")
