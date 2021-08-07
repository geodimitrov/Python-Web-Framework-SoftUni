from django.shortcuts import render

from book_center.bc_blog.models import BookCenterBlogPost


def show_blog_page(request):
    context = {
        'posts': BookCenterBlogPost.objects.all()
    }
    return render(request, 'blog/blog_page.html', context)


def show_blog_post(request, slug):
    context = {
        'post': BookCenterBlogPost.objects.get(slug=slug)
    }
    return render(request, 'blog/blog_post.html', context)
