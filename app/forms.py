from django import forms
from .models import Equipo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'
        

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
