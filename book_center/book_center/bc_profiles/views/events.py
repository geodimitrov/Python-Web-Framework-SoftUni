from book_center.bc_events.models import BookCenterEvent
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class MyEventsView(LoginRequiredMixin, ListView):
    template_name = 'profiles/events/my_events.html'
    context_object_name = 'events'
    model = BookCenterEvent
