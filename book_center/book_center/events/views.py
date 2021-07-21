from django.shortcuts import render


def show_events_view(request):
    return render(request, 'events/events.html', {})
