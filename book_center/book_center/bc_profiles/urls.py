from django.urls import path
from book_center.bc_profiles.views.profiles import ProfileMainView, ChangePasswordView, edit_profile_view
from book_center.bc_profiles.views.events import MyEventsView
from book_center.bc_profiles.views.discussions import discussion_details_view, CreateDiscussionView, \
    EditDiscussionView, DeleteDiscussionView, AllDiscussionsView, LikeCommentView, delete_comment_view


urlpatterns = [
    path('profile-dashboard/<username>', ProfileMainView.as_view(), name='profile main'),
    path('edit-profile/<username>', edit_profile_view, name='edit profile'),
    path('discussions/all', AllDiscussionsView.as_view(), name='show all discussions'),
    path('discussions/discussion-details/<pk>', discussion_details_view, name='discussion details'),
    path('discussions/create-discussion', CreateDiscussionView.as_view(), name='create discussion'),
    path('discussions/edit-discussion/<pk>', EditDiscussionView.as_view(), name='edit discussion'),
    path('discussions/delete-discussion/<pk>', DeleteDiscussionView.as_view(), name='delete discussion'),
    path('discussions/discussion-details/like/<pk>/', LikeCommentView.as_view(), name='like discussion'),
    path('discussions/discussion-details/<pk>/delete-comment/<comment_id>', delete_comment_view, name='delete comment'),
    path('my-events/<username>', MyEventsView.as_view(), name='show my events'),
    path('change-password/<username>', ChangePasswordView.as_view(), name='change password'),
]