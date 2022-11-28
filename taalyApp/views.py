from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .models import Planta

# Create your views here.

@login_required
def index(request):
    return render(request, 'taalyApp/index.html')

@login_required
def catalogo(request):
    cardGeneradas = Planta.objects.all()
    return render(request, 'taalyApp/catalogo.html', {'cards': cardGeneradas})

@login_required
def listarPlantas(request):
    plantasListadas = Planta.objects.all()
    return render(request, 'taalyApp/listarPlantas.html', {'plantas': plantasListadas})

@login_required
def eliminarPlanta(request, id):
    planta = Planta.objects.get(id = id)
    planta.delete()

    return redirect('/catalogo/listar')

@login_required
def registrarPlanta(request):
    nombre = request.POST['txtNombre']
    region = request.POST['txtRegion']
    efectos = request.POST['txtEfectos']
    usos = request.POST['txtUsos']
    descripcion = request.POST['txtDescripcion']

    planta = Planta.objects.create(nombre = nombre, region = region, efectos = efectos, usos = usos, descripcion = descripcion)

    return redirect('/catalogo/listar')

@login_required
def edicionPlanta(request):
    id = request.POST['inputHiddenID']
    nombre = request.POST['txtNombre']
    region = request.POST['txtRegion']
    efectos = request.POST['txtEfectos']
    usos = request.POST['txtUsos']
    descripcion = request.POST['txtDescripcion']

    planta = Planta.objects.get(id = id)

    planta.nombre = nombre
    planta.region = region
    planta.efectos = efectos
    planta.usos = usos
    planta.descripcion = descripcion
    planta.save()

    return redirect('/catalogo/listar')

    #planta = Planta.objects.create(nombre = nombre, region = region, efectos = efectos, usos = usos, descripcion = descripcion)

    return redirect('/catalogo/listar')

@login_required
def formRegistrarPlantas(request):
    return render(request, 'taalyApp/formRegistrarPlanta.html')

@login_required
def editarPlanta(request, id):
    planta = Planta.objects.get(id = id)
    data = {
        'titulo': 'Editar planta',
        'planta': planta
    }

    return render(request, 'taalyApp/formEditarPlanta.html', data)

# --------------------------------

def signup(request):
    if request.method == 'GET':
        return render(request, 'taalyApp/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('/inicio/')
            except IntegrityError:
                return render(request, 'taalyApp/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'taalyApp/register.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def signin(request):
    if request.method == 'GET':
        return render(request, 'taalyApp/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'taalyApp/signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('/inicio/')


@login_required
def signout(request):
    logout(request)
    return redirect('/signin/')