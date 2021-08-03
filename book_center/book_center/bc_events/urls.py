from django.urls import path
from book_center.bc_events.views import show_events_page, show_book_of_month, register_for_event

urlpatterns = [
    path('', show_events_page, name='show events'),
    path('book-of-the-month/', show_book_of_month, name='show book of month'),
    path('register/<pk>', register_for_event, name='register for event')
]