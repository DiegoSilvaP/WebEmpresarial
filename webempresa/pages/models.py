from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    # De la librería ckeditor, podemos introducir un completo editor de texto estilo word
    content = RichTextField(verbose_name="Contenido")
    # Este campo lo usaremos para una ordenación manual de los enlaces
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        # ordenamiento
        # Queremos que primero se muestren los "order" mas pequeños
        # Ahora toca modificar el panel de admin, para mostrar esa ordenación
        ordering = ["order","title"]

    def __str__(self):
        return self.title