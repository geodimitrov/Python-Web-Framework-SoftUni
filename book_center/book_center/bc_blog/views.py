from django.shortcuts import render
from book_center.bc_blog.models import BlogPost


def show_blog_page(request):
    context = {
        'posts': BlogPost.objects.all()
    }
    return render(request, 'blog/blog_page.html', context)


def show_blog_post(request, slug):
    context = {
        'post': BlogPost.objects.get(slug=slug)
    }
    return render(request, 'blog/blog_post.html', context)
