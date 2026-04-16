from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tareas, name='tareas'),
    path('nueva/', views.crear_tarea, name='crear_tarea'),
]