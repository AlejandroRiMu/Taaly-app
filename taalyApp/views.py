from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Planta

# Create your views here.

#@login_required
def index(request):
    return render(request, 'taalyApp/index.html')

def catalogo(request):
    return render(request, 'taalyApp/catalogo.html')

def listarPlantas(request):
    plantasListadas = Planta.objects.all()
    return render(request, 'taalyApp/listarPlantas.html', {'plantas': plantasListadas})

def eliminarPlanta(request, id):
    planta = Planta.objects.get(id = id)
    planta.delete()

    return redirect('/catalogo/listar')

def registrarPlanta(request):
    nombre = request.POST['txtNombre']
    region = request.POST['txtRegion']
    efectos = request.POST['txtEfectos']
    usos = request.POST['txtUsos']
    descripcion = request.POST['txtDescripcion']

    planta = Planta.objects.create(nombre = nombre, region = region, efectos = efectos, usos = usos, descripcion = descripcion)

    return redirect('/catalogo/listar')

def formRegistrarPlantas(request):
    return render(request, 'taalyApp/formRegistrarPlanta.html')