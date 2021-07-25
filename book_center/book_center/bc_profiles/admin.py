from django.contrib import admin
from django.contrib.admin import ModelAdmin
from book_center.bc_profiles.models import BookCenterUserProfile


@admin.register(BookCenterUserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name')

