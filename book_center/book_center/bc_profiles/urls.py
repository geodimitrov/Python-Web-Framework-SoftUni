from django.urls import path
from book_center.bc_profiles.views import CreateProfileView, show_all_profiles

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('all/', show_all_profiles, name='all profiles'),
]