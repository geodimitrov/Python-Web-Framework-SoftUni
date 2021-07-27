from book_center.bc_contact.models import ContactFormModel
from django.contrib.admin import ModelAdmin
from django.contrib import admin


@admin.register(ContactFormModel)
class ContactFormAdmin(ModelAdmin):
    list_display = ('subject', 'email', 'date_received', 'reply')
    ordering = ('reply', 'date_received')
    readonly_fields = ('date_received',)
