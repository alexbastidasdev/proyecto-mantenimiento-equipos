import datetime
from django import forms
from .models import Equipo, Tecnico, Mantenimiento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('nombre', 'marca', 'dependencia', 'periodicidad_mantenimiento', 'proximo_mantenimiento', 'estado_equipo')


class MantenimientoForm(forms.ModelForm):

    class Meta:
        model = Mantenimiento
        fields = '__all__'


class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico
        fields = '__all__'
  

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
