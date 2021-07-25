from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def show_events_view(request):
    return render(request, 'events/events.html', {})
