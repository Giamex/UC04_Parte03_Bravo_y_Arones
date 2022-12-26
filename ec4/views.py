from django.shortcuts import render, HttpResponse, redirect
from ec4.models import Curso
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Evidencia de Capacidad 4'
    })

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html',{
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })

def crear_curso(request):
    return render(request, 'crear_curso.html',{
        'titulo': 'Agregar Curso'
    })

def eliminar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('cursos')

def save_curso(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        horas = request.POST['horas']
        credito = request.POST['credito']
        estado = request.POST['estado']
 
        curso = Curso(
            codigo = codigo,
            nombre = nombre,
            horas = horas,
            creditos = credito,
            estado = estado
        )
        curso.save()
        # Crear un mensaje flash (Sesión que solo se muestra 1 vez)
        messages.success(request, f'Se agregó correctamente el curso {curso.id}')
        return redirect('cursos')
    else:
        return HttpResponse("<h2>No se ha podido registrar el curso</h2>")


def carreras(request):
    return render(request, 'carreras.html')

def crear_carrera(request):
    return render(request, 'crear_carrera.html')

def eliminar_carrera(request):
    return render(request, 'eliminar_carrera.html')

