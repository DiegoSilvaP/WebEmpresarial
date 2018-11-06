from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["name"]

    def __str__(self):
        return self.name