from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from book_center.bc_main.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'main/home.html'


class AboutView(TemplateView):
    template_name = 'main/about.html'


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
