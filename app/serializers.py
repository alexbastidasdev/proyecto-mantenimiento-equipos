from rest_framework import serializers
from .models import Equipo, Tecnico, Mantenimiento

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = "__all__"

        
class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = "__all__"


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = "__all__"
