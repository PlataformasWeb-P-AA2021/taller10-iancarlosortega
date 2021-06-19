"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('parroquias', views.listado_parroquias, name="listado_parroquias"),
        path('crear_parroquia', views.crear_parroquia, 
            name='crear_parroquia'),
        path('editar_parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
        path('barrios', views.listado_barrios, name="listado_barrios"),
        path('crear_barrio', views.crear_barrio, 
            name='crear_barrio'),
        path('editar_barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
        path('crear/barrio_parroquia/<int:id>', 
            views.crear_barrio_parroquia, 
            name='crear_barrio_parroquia'),
 ]
