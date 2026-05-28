from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Etiqueta(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=50)
    color = models.CharField(_("Color"), max_length=30)

    def __str__(self):
        return f"Etiqueta: {self.nombre}"

    class Meta:
        verbose_name = _("Etiqueta")
        verbose_name_plural = _("Etiquetas")


class Tarea(models.Model):
    nombre = models.CharField(_("Nombre de la Tarea"), max_length=100)
    completada = models.BooleanField(
        _("Tarea Completada"),
        default=False,
        help_text=_("¿La tarea está completada?"),
    )
    fecha_completado = models.DateField(_("Fecha de Completado"))
    fecha_creacion = models.DateTimeField(_("Fecha de Creación"), auto_now=True)
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="responsable",
        default=None,
        blank=True,
        null=True,
        verbose_name=_("Responsable"),
    )
    etiqueta = models.ManyToManyField(
        Etiqueta,
        default=None,
        blank=True,
        related_name="etiquetas",
        verbose_name=_("Etiqueta"),
    )
    activo = models.BooleanField(
        _("Activo"),
        default=True,
        help_text=_("Verdadero si NO está archivado"),
    )
    imagen = models.ImageField(
        _("Imagen"),
        upload_to="card_image/",
        null=True,
        blank=True,
    )

    def nombre_mayuscula(self):
        return f"{self.nombre.upper()}"

    def __str__(self):
        return f"Soy la tarea: {self.nombre}"

    class Meta:
        verbose_name = _("Tarea de proyecto")
        verbose_name_plural = _("Tareas de los proyectos")
        ordering = ["-id"]


# si creo o modifico un modelo, debo correr:
# > python3 manage.py makemigrations
# > python3 manage.py migrate