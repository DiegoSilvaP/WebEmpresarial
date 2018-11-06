from django.shortcuts import render, get_object_or_404
from .models import Category, Post, User

# Create your views here.}

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    # Qué pasa si el usuario ingresa un ID que no existe? bueno, que django explotará; por lo que es una buena idea mostrar el error (404)
    # en vez de que django se explote
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category,})

