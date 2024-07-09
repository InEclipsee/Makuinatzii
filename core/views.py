from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from core.models import Publicacion, Servicio
from core.forms import FormPublicacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    context = {'dataPosts': dataPosts,
               'user': request.user,
               'groups': request.user.groups.all()}
    return render(request, 'core/galeria.html', context)

def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url="/accounts/login/")
def profile(request):
    context = {'user': request.user,
               'groups': request.user.groups.all()}
    return render(request, 'core/profile.html', context)

def formularioPublicacion(request):
    form = FormPublicacion()
    if request.method == 'POST':
        form = FormPublicacion(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(user=request.user)
            return redirect('galeria')
    else:
        form = FormPublicacion(request.POST, request.FILES)
    context = {'form': form}
    return render(request, 'core/add.html', context)

def updateView(request, fP_id):
    pub = Publicacion.objects.get(id=fP_id)
    form = FormPublicacion(instance=pub)
    if request.method == 'POST':
        form = FormPublicacion(request.POST, request.FILES, instance=pub)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    context = {'form': form}
    return render(request, 'core/add.html', context)

def deleteView(request, fP_id):
    pub = Publicacion.objects.get(id=fP_id)
    if request.method == 'POST':
        pub.delete()
        return redirect('galeria')
    context = {'pub': pub}
    return render(request, 'core/delete.html', context)

def logout_view(request):
    logout(request)
    return redirect('inicio')