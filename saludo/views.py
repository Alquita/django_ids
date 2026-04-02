from django.shortcuts import HttpResponse
from django.shortcuts import render
#vistas, lógica de negocio, procesamiento de datos, etc

contexto = {"nombre": "Juan",
            "esMayor": True,
            "mascotas": ["Perro", "Gato", "Pájaro"]
            }
def saludo(request):
    return render(request, "saludo/index.html", contexto)

def  despedir(request):
    return render(request, "saludo/despedir.html", contexto)

def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi sitio web</h1>")