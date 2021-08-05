from book_center.bc_profiles.models.discussions import BookCenterDiscussion
from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(BookCenterUserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'profile_image')


@admin.register(BookCenterDiscussion)
class BookCenterDiscussionAdmin(ModelAdmin):
    list_display = ('title', 'topic',)