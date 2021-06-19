from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py 
from ordenamiento.forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def listado_parroquias(request):
    """
        Listar los registros del modelo Parroquia, 
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # parroquias
    parroquias = Parroquia.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquias}
    return render(request, 'listado_parroquias.html', informacion_template)

def listado_barrios(request):
    """
        Listar los registros del modelo Barrio, 
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # barrios
    barrios = Barrio.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'barrios': barrios}
    return render(request, 'listado_barrios.html', informacion_template)


def crear_parroquia(request):

    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listado_parroquias)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario) 


def editar_parroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listado_parroquias)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 


def crear_barrio(request):

    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listado_barrios)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario) 


def editar_barrio(request, id):

    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listado_barrios)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario) 

def crear_barrio_parroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listado_parroquias)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario) 




