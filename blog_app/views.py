from django.shortcuts import render, get_object_or_404
from blog_app.models import Blog

# Create your views here.

def blog(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': blogs})


def blog_all(request):
    blogs = Blog.objects
    return render(request, 'blog-all.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog-detail.html', {'blog': blog})