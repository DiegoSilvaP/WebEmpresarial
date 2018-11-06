from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # Modificamos la forma en la que se muestran las paginas y le agregamos el orden
    list_display = ('title', 'order')

admin.site.register(Page, PageAdmin)
