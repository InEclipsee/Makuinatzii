from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from core.models import publicacion
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    return render(request, 'core/profile.html')