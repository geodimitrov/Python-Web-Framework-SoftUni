from django.urls import path
from book_center.bc_profiles.views import profile_details_view, edit_profile_view, profile_main_view

urlpatterns = [
    path('dashboard/<username>', profile_main_view, name='profile main'),
    path('profile-details/<username>', profile_details_view, name='profile details'),
    path('edit-profile/', edit_profile_view, name='edit profile',)
]