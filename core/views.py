from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def perfil(request):
    return render(request, 'core/perfil.html')