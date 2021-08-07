from book_center.bc_contact.forms import ContactForm
from book_center.bc_contact.models import BookCenterContactFormModel
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


class ContactFormView(CreateView):
    template_name = 'contact/contact_form.html'
    model = BookCenterContactFormModel
    form_class = ContactForm
    success_url = reverse_lazy('submit contact')


class SubmitContactFormView(TemplateView):
    template_name = 'contact/submit_contact.html'
