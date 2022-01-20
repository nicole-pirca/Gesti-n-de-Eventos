from django.shortcuts import render
from django.http import HttpResponse

from servicios.models import Servicio


def home(request):
   #appweb/projectpp/template/projectpp/home.html
   #C:/Users/Familia/Documents/NICOLE/Django/appweb/projectpp/template/projectpp/home.html
    return render(request,"projectpp/home.html")


def tienda(request):
    return render(request,"projectpp/tienda.html")



def contacto(request):
    return render(request,"projectpp/contacto.html")
    
