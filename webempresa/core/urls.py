from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home, name="home"),
    path('about/', core_views.about, name="about"),
    # path('services/', core_views.services, name="services"),
    path('store/', core_views.store, name="store"),
    # path('contact/', core_views.contact, name="contact"),
    # path('blog/', core_views.blog, name="blog"),
    # path('sample/', core_views.sample, name="sample"),
]