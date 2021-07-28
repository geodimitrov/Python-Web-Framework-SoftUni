from django.shortcuts import render


def show_blog_page(request):
    return render(request, 'blog/blog_page.html')
