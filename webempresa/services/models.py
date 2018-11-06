from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
# NOTA: Los modelos deben ir en SINGULAR
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to="services", verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    
    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.title