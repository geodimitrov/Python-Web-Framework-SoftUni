from book_center.bc_profiles.models.discussions import BookCenterDiscussion, BookCenterDiscussionComment
from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from book_center.bc_profiles.forms.discussions import DiscussionForm, DiscussionCommentForm
from book_center.bc_profiles.forms.profiles import UserProfileForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(BookCenterUserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'profile_image')
    readonly_fields = ('user',)
    form = UserProfileForm


@admin.register(BookCenterDiscussion)
class DiscussionAdmin(ModelAdmin):
    list_display = ('title', 'topic', 'created_on')
    readonly_fields = ('author', 'created_on', )
    form = DiscussionForm


@admin.register(BookCenterDiscussionComment)
class DiscussionCommentAdmin(ModelAdmin):
    list_display = ('comment', 'discussion', 'created_on')
    fieldsets = (
        (None, {'fields': ('comment', 'discussion', 'author', 'created_on')}),
    )
    readonly_fields = ('author', 'created_on',  )
    form = DiscussionCommentForm
