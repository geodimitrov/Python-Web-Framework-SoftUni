from django.shortcuts import render
from book_center.bc_events.models import BookCenterEvent


def show_events_page(request):
    context = {
        'book_of_month': BookCenterEvent.objects.filter(is_book_of_month=True),
        'events': BookCenterEvent.objects.all()
    }
    return render(request, 'events/events.html', context)


def show_book_of_month(request):
    context = {
        'book_of_month': BookCenterEvent.objects.filter(is_book_of_month=True).first()
    }
    return render(request, 'events/book_of_the_month.html', context)


def register_for_event(request, pk):
    context = {

    }
    return render(request, 'events/register_for_event.html', context)