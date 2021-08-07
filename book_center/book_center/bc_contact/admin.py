from book_center.bc_contact.models import BookCenterContactFormModel
from django.contrib.admin import ModelAdmin
from django.contrib import admin


@admin.register(BookCenterContactFormModel)
class ContactFormAdmin(ModelAdmin):
    list_display = ('subject', 'email', 'date_received', 'reply')
    ordering = ('reply', 'date_received')
    readonly_fields = ('date_received',)
