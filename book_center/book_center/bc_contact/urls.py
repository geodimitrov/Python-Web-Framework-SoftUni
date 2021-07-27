from book_center.bc_contact.views import ContactFormView, SubmitContactFormView
from django.urls import path


urlpatterns = [
    path('', ContactFormView.as_view(), name='contact'),
    path('form-submitted-successfully/', SubmitContactFormView.as_view(), name='submit contact'),
]