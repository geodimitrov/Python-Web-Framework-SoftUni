from book_center.bc_events.models import BookCenterEvent, BookCenterEventRegister
from book_center.bc_events.forms import BookCenterEventForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin


@admin.register(BookCenterEvent)
class EventsAdmin(ModelAdmin):
    list_display = ('title', 'category', 'is_book_of_month', 'event_date')
    form = BookCenterEventForm


@admin.register(BookCenterEventRegister)
class EventLogAdmin(ModelAdmin):
    list_display = ('event', 'participant', 'registration_date')
    fieldsets = (
        (None, {'fields': ('event', 'participant', 'registration_date')}),
    )
    readonly_fields = ('registration_date',)
