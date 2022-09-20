from django.contrib import admin
from .models import Equipo, Tecnico, Mantenimiento

# Register your models here.
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'fecha_ingreso', 'dependencia', 'periodicidad_mantenimiento', 'proximo_mantenimiento', 'estado_equipo')
    list_filter = ('nombre', 'marca', 'fecha_ingreso', 'dependencia', 'periodicidad_mantenimiento', 'estado_equipo')
    search_fields = ('nombre', 'marca', 'fecha_ingreso', 'dependencia', 'periodicidad_mantenimiento', 'estado_equipo')

class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'cedula', 'telefono', 'empresa')
    list_filter = ('nombre', 'apellidos', 'cedula', 'telefono', 'empresa')
    search_fields = ('nombre', 'apellidos', 'cedula', 'telefono', 'empresa')

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('tipo_mantenimiento', 'fecha_mantenimiento', 'observaciones', 'equipo', 'tecnico')
    list_filter = ('tipo_mantenimiento', 'fecha_mantenimiento', 'observaciones', 'equipo', 'tecnico')
    search_fields = ('tipo_mantenimiento', 'fecha_mantenimiento', 'observaciones', 'equipo', 'tecnico')

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Tecnico, TecnicoAdmin)
admin.site.register(Mantenimiento, MantenimientoAdmin)
