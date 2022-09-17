from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import EquipoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import EquipoSerializer 

# Create your views here.

# views template
def index(request):
    return render(request, 'index.html')

@login_required
def listar_equipos(request):
    equipos = Equipo.objects.all()
    data = {
        'equipos': equipos
    }
    return render(request, 'equipos/listar.html', data)
    
@login_required
def agregar_equipo(request):
    data = {
        'form': EquipoForm()
    }

    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo Agregado Correctamente")
            return redirect(to="listar_equipos")
        
        data["form"] = formulario 

    return render(request, 'equipos/agregar.html', data)

@login_required
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    data = {
        'form': EquipoForm(instance=equipo)
    }

    if request.method == 'POST':
        formulario = EquipoForm(data=request.POST, instance=equipo)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo Editado Correctamente")
            return redirect(to="listar_equipos")

        data["form"] = formulario
        
    return render(request, 'equipos/editar.html', data)

@login_required
def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    messages.success(request, "Equipo Eliminado Correctamente")
    return redirect(to="listar_equipos")

def tecnicos(request):
    return render(request, 'tecnicos.html')

def mantenimientos(request):
    return render(request, 'mantenimientos.html')

def contacto(request):
    return render(request, 'contacto.html')

def privacidad(request):
    return render(request, 'privacidad.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has Registrado Correctamente")
            return redirect(to="index")
        
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)



# views api
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer