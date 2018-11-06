from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    # Vamos a personalizar un poco mas el panel de administración
    # Indicamos los campos que queremos mostrar en la lista de entradas
    list_display = ('title', 'author', 'published','post_categories')
    # También se puede h acer una ordenación
    # Aquí estamos indicando que primero ordene por autor de forma alfabética y dentro, que ordene por la fecha de publicación
    ordering = ('author', 'published')
    # Se puede agregar un campo de búsqueda
    # NOTA. es importante que cuando se ahce la búsqueda hacia otro modelo, se establezca el campo a buscar, de lo contrario
    # django no sabrá qué campo buscar del modelo de autor
    search_fields = ('title','content', 'author__username', 'categories__name')
    # Se puede hacer un filtro por jerarquía de fecha
    date_hierarchy = ('published')
    # Otra cosa interesante, es una lista de filtros, es más lógico hacer un filtro por relaciones
    # pues no tendría mucho sentido filtrar por título, pero sí por autor
    list_filter = ('author__username','categories__name')

    # Si en la lista queremos listar las categorías de cada post, debemos crear un método
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    # Para cambiar el nombre genérico "Post categories"
    post_categories.short_description ="Categorías"



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
    