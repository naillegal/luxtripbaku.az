from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

def blog(request):
    blogs = Blog.objects.all().order_by('-created')
    paginator = Paginator(blogs, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'blogs':blogs, 'page_obj': page_obj})

def blog_detail(request, pk, slug):
    blog = get_object_or_404(Blog, pk=pk, slug=slug)
    return render(request, 'blog-detail.html', {'blog': blog})