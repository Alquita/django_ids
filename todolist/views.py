from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "todolist/tareas.html", {"tareas": tareas})

def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
        form = TareaForm()
    
    return render(request, "todolist/crear_tarea.html", {"form": form})

#param ruta: url.com/usuarios/5
#query param: url.com/usuarios?clave=valorclave_dos=valorclave_tres=valor

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == "POST":
        form = TareaForm(request.POST, request.FILES, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("tareas")
    else:
     
        form = TareaForm(instance=tarea)
    
    return render(request, 'todolist/editar_tarea.html', {"form": form})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == "POST":
        tarea.activo = False
        tarea.save()
        return redirect("tareas")
    else:
        return render(request, "todolist/eliminar_tarea.html", {"tarea": tarea})
    

