from django.urls import path
from book_center.bc_auth.views import sign_up_view, sign_in_view, sign_out_view


urlpatterns = [
    path('sign-up/', sign_up_view, name='sign up'),
    path('sign-in/', sign_in_view, name='sign in'),
    path('sign-out/', sign_out_view, name='sign out'),
]