from django.contrib import admin
from django.contrib.admin import ModelAdmin
from book_center.bc_blog.models import BlogPost, BlogPostAuthor


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('date_created',)


@admin.register(BlogPostAuthor)
class BlogPostAuthorAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')