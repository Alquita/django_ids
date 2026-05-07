from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def registrarse(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("saludo")
    else:
        form = UserCreationForm()
    
    return render(request, "registration/register.html", {"form": form})




@login_required
def tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "todolist/tareas.html", {"tareas": tareas})



@login_required
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
@login_required
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
@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if request.method == "POST":
        tarea.activo = False
        tarea.save()
        return redirect("tareas")
    else:
        return render(request, "todolist/eliminar_tarea.html", {"tarea": tarea})
    


