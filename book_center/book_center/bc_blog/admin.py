from book_center.bc_blog.models import BookCenterBlogPost, BookCenterBlogPostAuthor
from django.contrib.admin import ModelAdmin
from django.contrib import admin


@admin.register(BookCenterBlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'date_created')
    readonly_fields = ('date_created',)


@admin.register(BookCenterBlogPostAuthor)
class BlogPostAuthorAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')