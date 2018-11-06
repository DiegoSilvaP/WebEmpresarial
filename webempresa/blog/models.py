from django.db import models
# Importar la librería timezone
# from django.utils import timezone
from django.utils.timezone import now
# Importar el model de autenticación y usuarios de django
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    
    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    # Establecida por el autor y por defecto tendrá la hora actual
    # NOTA esta es una forma correcta de registrar la hora actual, pero django estará esperando que coloquemos directamente el now, importando
    # django.utils.timezone.now en ves de from django.utils import timezone
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", blank=True, null=True)
    # Se enlazará con una clave foránea tomándola del modelo de usuarios de django
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # Se relacionará con varias categorias, (ya las tenemos arriba)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.title

