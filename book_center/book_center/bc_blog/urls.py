from django.urls import path
from book_center.bc_blog.views import show_blog_page

urlpatterns = [
    path('', show_blog_page, name='show blog page')
]