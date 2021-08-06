from django.urls import path
from book_center.bc_profiles.views.discussions import discussions_view, discussion_details_view, edit_discussion_view
from book_center.bc_profiles.views.profiles import ProfileMainView, ChangePasswordView, profile_details_view
from book_center.bc_profiles.views.views import my_library_view, my_events_view

urlpatterns = [
    path('dashboard/<username>', ProfileMainView.as_view(), name='profile main'),
    path('profile-details/<username>', profile_details_view, name='profile details'),
    path('discussions/all', discussions_view, name='show discussions'),
    path('discussions/discussion/<pk>', discussion_details_view, name='discussion details'),
    path('discussions/edit-discussion/<pk>', edit_discussion_view, name='edit discussion'),
    path('my-library/<username>', my_library_view, name='show my library'),
    path('my-events/<username>', my_events_view, name='show my events'),
    path('change-password/<username>', ChangePasswordView.as_view(), name='change password'),
]