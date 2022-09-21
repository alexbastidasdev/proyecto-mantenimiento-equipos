from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('equipos', EquipoViewSet)
router.register('tecnicos', TecnicoViewSet)
router.register('mantenimientos', MantenimientoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('privacidad/', privacidad, name='privacidad'),
    path('equipos/', listar_equipos, name='listar_equipos'),
    path('agregar-equipo/', agregar_equipo, name='agregar_equipo'),
    path('editar-equipo/<id>/', editar_equipo, name='editar_equipo'),
    path('eliminar-equipo/<id>/', eliminar_equipo, name='eliminar_equipo'),
    path('mantenimientos/', listar_mantenimientos, name='listar_mantenimientos'),
    path('agregar-mantenimiento/', agregar_mantenimiento, name='agregar_mantenimiento'),
    path('editar-mantenimiento/<id>/', editar_mantenimiento, name='editar_mantenimiento'),
    path('eliminar-mantenimiento/<id>/', eliminar_mantenimiento, name='eliminar_mantenimiento'),
    path('tecnicos/', listar_tecnicos, name='listar_tecnicos'),
    path('agregar-tecnico/', agregar_tecnico, name='agregar_tecnico'),
    path('editar-tecnico/<id>/', editar_tecnico, name='editar_tecnico'),
    path('eliminar-tecnico/<id>/', eliminar_tecnico, name='eliminar_tecnico'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),

]
