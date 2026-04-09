from django.shortcuts import HttpResponse
from django.shortcuts import render
from todolist.models import Tarea
#vistas, lógica de negocio, procesamiento de datos, etc

def saludo(request):
    tareas = Tarea.objects.filter()

    return render(request, "saludo/index.html", dict(tareas=tareas))

def  despedir(request):
    return render(request, "saludo/despedir.html")

def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi sitio web</h1>")