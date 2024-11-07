from django.shortcuts import render, redirect
from .models import Persona


def listar_usuarios(request):
    usuarios = Persona.objects.all()
    modificar_usuario = None

    if 'editando' in request.GET:
        id_usuario = request.GET['editando']
        modificar_usuario = Persona.objects.get(pk=id_usuario)

    return render(request, 'agenda.html', {"usuarios": usuarios, "modificar_usuario": modificar_usuario})


def crear_usuario(request):
    if request.method == "POST":
        Persona.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            edad=request.POST['edad'],
            rut=request.POST['rut']
        )
    return redirect("listar_usuarios")


def editar_usuario(request, id_usuario):
    if request.method == 'POST':
        Persona.objects.filter(id=id_usuario).update(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            edad=request.POST['edad'],
            rut=request.POST['rut']
        )
    return redirect("listar_usuarios")


def eliminar_usuario(request, id_usuario):
    Persona.objects.get(id=id_usuario).delete()
    return redirect("listar_usuarios")
