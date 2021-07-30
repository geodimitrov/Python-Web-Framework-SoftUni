from django.urls import path
from book_center.bc_auth.views import SignUpView, SignInView, SignOutView, \
    VerifyEmailSignUpView, activate_email_view, VerifyEmailSignInView, verify_email_sign_in_view

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('verify-email-sign-up/', VerifyEmailSignUpView.as_view(), name='verify email initial'),
    path('verify-email-sign-in/<pk>', verify_email_sign_in_view, name='verify email additional'),
    path('activate-email/<pk>/<token>/', activate_email_view, name='activate email'),
]