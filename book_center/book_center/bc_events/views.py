from book_center.bc_events.models import BookCenterEvent, BookCenterEventRegister
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def show_events_page_view(request):
    context = {
        'book_of_month': BookCenterEvent.objects.filter(is_book_of_month=True),
        'events': BookCenterEvent.objects.all()
    }
    return render(request, 'events/events.html', context)


def show_book_of_month_view(request):
    context = {
        'book_of_month': BookCenterEvent.objects.filter(is_book_of_month=True).first()
    }
    return render(request, 'events/book_of_the_month.html', context)


@login_required(login_url='require sign in')
def register_for_event_view(request, pk):
    event = BookCenterEvent.objects.get(pk=pk)
    event_register = BookCenterEventRegister(
        event=event,
        participant=request.user
    )

    try:
        event_register.save()
    except:
        return render(request, 'events/already_registered_for_event.html')

    return render(request, 'events/register_for_event.html')