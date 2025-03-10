from django.shortcuts import render
from .models import Project
from blog.models import Post

# Create your views here.

def home(request):
    projects = Project.objects.all()
    posts = Post.objects.all()[:6]
    return render(request, 'portfolio/home.html', {'projects': projects, 'posts': posts})  # Added context dictionary