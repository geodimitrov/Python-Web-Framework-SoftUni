from django.shortcuts import render, redirect
from book_center.main.forms import ContactForm


def home_view(request):
    return render(request, 'main/home.html', {})


def about_view(request):
    return render(request, 'main/about.html', {})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('home')

    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'main/contact.html', context)
