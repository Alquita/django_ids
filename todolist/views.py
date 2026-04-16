from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Tarea
from .forms import TareaForm

def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "todolist/tareas.html", {"tareas": tareas})

def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TareaForm()
    
    return render(request, "todolist/crear_tarea.html", {"form": form})