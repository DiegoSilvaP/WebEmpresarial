# La idea de extender el contexto, es poder acceder a nuestro diccionario desde cualquier template, inyectándolo en el contexto global
# Para extender el procesador de contexto, en settings, en el apartado de procesador de contexto, agregamos, este procesador
# ahora podemos acceder desde cualquier template al diccionario desde la clave LINK_TWITTER o LINK_FACEBOOK o incluso LINK_INSTAGRAM

from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx