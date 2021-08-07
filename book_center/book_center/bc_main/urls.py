from book_center.bc_main.views import HomeView, AboutView
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
