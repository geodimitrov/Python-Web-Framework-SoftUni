from django.contrib.auth.decorators import login_required
from django.shortcuts import render



@login_required()
def my_events_view(request, username):
    return render(request, 'profiles/events/my_events.html')