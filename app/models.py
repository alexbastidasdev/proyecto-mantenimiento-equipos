from django.db import models
from django.urls import reverse

# Create your models here.
class Equipo(models.Model):

    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fecha_ingreso = models.DateField(auto_now_add=True)
    dependencia = models.CharField(max_length=50)
    periodicidad_mantenimiento = models.IntegerField()
    proximo_mantenimiento = models.DateField()
    estado_equipo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class Tecnico(models.Model):

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    empresa = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nombre

class Mantenimiento(models.Model):

    tipo_mantenimiento = models.CharField(max_length=50)
    fecha_mantenimiento = models.DateField(auto_now_add=True)
    observaciones = models.TextField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE )
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_manteniento
