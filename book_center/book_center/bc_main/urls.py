from django.urls import path
from book_center.bc_main.views import contact_view, HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact_view, name='contact'),
]