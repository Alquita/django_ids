from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completada = models.BooleanField(default=False, help_text="la tarea esta completada?", verbose_name="Tarea Completada")
    fecha_completado = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    responsable  = models.ForeignKey(
        User, on_delete=models.CASCADE, 
        related_name="responsable", 
        default= None, 
        blank=True, 
        null=True,
    )
    etiqueta = models.ManyToManyField(Etiqueta, default=None, blank=True, null=True)
    activo = models.BooleanField(default=True, help_text="Verdadero si esta activo, falso no esta eliminado", verbose_name="Tarea Activa")
    imagen = models.ImageField(upload_to = "card_image/", null=True, blank=True)


    def nombre_mayuscula(self):
        return self.nombre.upper()

    def __str__(self):
        return f"Soy la tarea: {self.nombre}"
    
    class Meta:
        verbose_name = "Tarea del proyecto"
        verbose_name_plural = "Tareas de los proyectos"
        ordering = ['id']

#si creo o modifico un modelo, debo correr:
# >python manage.py makemigrations
# >python manage.py migrate