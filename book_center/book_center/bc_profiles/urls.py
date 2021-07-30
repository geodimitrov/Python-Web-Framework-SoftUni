from django.urls import path
from book_center.bc_profiles.views import profile_details_view

urlpatterns = [
    path('profile-details/<pk>', profile_details_view, name='profile details'),
]