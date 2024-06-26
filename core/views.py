from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from core.models import Publicacion, Servicio
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    dataPosts = Publicacion.objects.all()
    dataServ = Servicio.objects.all()
    context = {'dataPosts': dataPosts, 'dataServ': dataServ}
    return render(request, 'core/index.html', context)

def contacto(request):
    return render(request, 'core/contacto.html')

def galeria(request):
    dataPosts = Publicacion.objects.all()
    context = {'dataPosts': dataPosts}
    return render(request, 'core/galeria.html', context)

def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request, 'core/profile.html')