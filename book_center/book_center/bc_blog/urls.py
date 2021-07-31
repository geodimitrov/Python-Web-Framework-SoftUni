from django.urls import path
from book_center.bc_blog.views import show_blog_page, show_blog_post

urlpatterns = [
    path('', show_blog_page, name='show blog page'),
    path('post/<str:slug>', show_blog_post, name='show blog post'),
]