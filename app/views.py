from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import EquipoForm, TecnicoForm, MantenimientoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import EquipoSerializer, TecnicoSerializer, MantenimientoSerializer
from django.db.models import Q

# Create your views here.

# views template
def index(request):
    return render(request, 'index.html')

# views equipos
@login_required
def listar_equipos(request):
    busqueda = request.GET.get('buscar')
    equipos = Equipo.objects.all()

    if busqueda:
        equipos = Equipo.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(marca__icontains=busqueda) |
            Q(dependencia__icontains=busqueda) |
            Q(periodicidad_mantenimiento__icontains=busqueda) |
            Q(proximo_mantenimiento__icontains=busqueda) |
            Q(estado_equipo__icontains=busqueda)
        ).distinct()

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

# views mantenimientos
@login_required
def listar_mantenimientos(request):
    busqueda = request.GET.get('buscar')
    mantenimientos = Mantenimiento.objects.all()

    if busqueda:
        mantenimientos = Mantenimiento.objects.filter(
            Q(tipo_mantenimiento__icontains=busqueda) |
            Q(observaciones__icontains=busqueda)
        ).distinct()

    data = {
        'mantenimientos': mantenimientos
    }
    return render(request, 'mantenimientos/listar.html', data)
    
@login_required
def agregar_mantenimiento(request):
    data = {
        'form': MantenimientoForm()
    }

    if request.method == 'POST':
        formulario = MantenimientoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mantenimiento Agregado Correctamente")
            return redirect(to="listar_mantenimientos")
        
        data["form"] = formulario 

    return render(request, 'mantenimientos/agregar.html', data)

@login_required
def editar_mantenimiento(request, id):
    mantenimiento = get_object_or_404(Mantenimiento, id=id)
    data = {
        'form': MantenimientoForm(instance=mantenimiento)
    }

    if request.method == 'POST':
        formulario = MantenimientoForm(data=request.POST, instance=mantenimiento)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mantenimiento Editado Correctamente")
            return redirect(to="listar_mantenimientos")

        data["form"] = formulario
        
    return render(request, 'mantenimientos/editar.html', data)

@login_required
def eliminar_mantenimiento(request, id):
    mantenimiento = get_object_or_404(Mantenimiento, id=id)
    mantenimiento.delete()
    messages.success(request, "Mantenimiento Eliminado Correctamente")
    return redirect(to="listar_mantenimientos")

# views tecnicos
@login_required
def listar_tecnicos(request):
    busqueda = request.GET.get('buscar')
    tecnicos = Tecnico.objects.all()

    if busqueda:
        tecnicos = Tecnico.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(cedula__icontains=busqueda) |
            Q(telefono__icontains=busqueda) |
            Q(empresa__icontains=busqueda)
        ).distinct()

    data = {
        'tecnicos': tecnicos
    }
    return render(request, 'tecnicos/listar.html', data)
    
@login_required
def agregar_tecnico(request):
    data = {
        'form': TecnicoForm()
    }

    if request.method == 'POST':
        formulario = TecnicoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tecnico Agregado Correctamente")
            return redirect(to="listar_tecnicos")
        
        data["form"] = formulario 

    return render(request, 'tecnicos/agregar.html', data)

@login_required
def editar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    data = {
        'form': TecnicoForm(instance=tecnico)
    }

    if request.method == 'POST':
        formulario = TecnicoForm(data=request.POST, instance=tecnico)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Técnico Editado Correctamente")
            return redirect(to="listar_tecnicos")

        data["form"] = formulario
        
    return render(request, 'tecnicos/editar.html', data)

@login_required
def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    tecnico.delete()
    messages.success(request, "Técnico Eliminado Correctamente")
    return redirect(to="listar_tecnicos")


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


class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer