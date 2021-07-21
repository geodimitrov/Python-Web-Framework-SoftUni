from django.urls import path
from book_center.events.views import show_events_view

urlpatterns = [
    path('', show_events_view, name='show events'),
]