from django.contrib import admin
from django.contrib.admin import ModelAdmin

from book_center.bc_events.forms import BookCenterEventForm
from book_center.bc_events.models import BookCenterEvent


@admin.register(BookCenterEvent)
class EventsAdmin(ModelAdmin):
    list_display = ('title',)
    form = BookCenterEventForm
