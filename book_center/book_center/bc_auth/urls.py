from django.urls import path
from book_center.bc_auth.views import SignUpView, SignInView, SignOutView, UserPasswordResetView, \
    VerifyEmailSignUpView, activate_email_view, verify_email_sign_in_view, UserPasswordResetDoneView, \
    UserPasswordResetConfirmView, UserPasswordResetCompleteView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('verify-email-sign-up/', VerifyEmailSignUpView.as_view(), name='verify email initial'),
    path('verify-email-sign-in/<pk>', verify_email_sign_in_view, name='verify email additional'),
    path('activate-email/<pk>/<token>/', activate_email_view, name='activate email'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset password'),
    path('reset-password/sent/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete')
]