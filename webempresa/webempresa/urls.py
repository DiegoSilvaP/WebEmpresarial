"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Para servir imagenes
from django.conf import settings

urlpatterns = [
    # paths de core
    path('', include('core.urls')),
    # paths de services
    path('services/', include('services.urls')),
     # paths de blog
    path('blog/', include('blog.urls')),
    # paths de pages
    path('page/', include('pages.urls')),
    # paths de contact
    path('contact/', include('contact.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = settings.ADMIN_SITE_HEADER

# Si Debug es true
if settings.DEBUG:
    # Nos permite cargar archivos estáticos
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)