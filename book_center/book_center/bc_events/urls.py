from django.urls import path
from book_center.bc_events.views import show_events_page_view, show_book_of_month_view, register_for_event_view

urlpatterns = [
    path('', show_events_page_view, name='show events'),
    path('book-of-the-month/', show_book_of_month_view, name='show book of month'),
    path('register/<pk>', register_for_event_view, name='register for event'),
]