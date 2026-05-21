
from datetime import datetime
from todolist.models import Etiqueta
from django.core.cache import cache

def year_context(request):
    year = datetime.now().year
    return {"year": year} #se retorna un diccionario con la clave "year"



def bienvenido_context (request):

    if request.user.is_authenticated:
        mensaje = f"Bienvenido {request.user.username} a mi sitio web!"

    else:
        mensaje = "Bienvenido a mi sitio web invitado, por favor inicia sesión para una mejor experiencia"


    return {'mensaje_bienvenida': mensaje}



def etiquetas_context(request):
    etiquetas = cache.get("todolist_etiquetas")
    if etiquetas is None:
        etiquetas = Etiqueta.objects.all()
        cache.set("todolist_etiquetas", etiquetas, 3600 * 24) #setea la cache por 24 horas (3600 segundos * 24 horas)
        #print ('nueva cache seteada')
    return {"etiquetas_populares": etiquetas}

