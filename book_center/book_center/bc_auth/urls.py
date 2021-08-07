from django.urls import path
from book_center.bc_auth.views.auth import SignUpView, SignInView, SignOutView, \
    RequireSignInView
from book_center.bc_auth.views.email_verification import VerifyEmailSignUpView, \
    verify_email_sign_in_view, activate_email_view
from book_center.bc_auth.views.password_reset import UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('verify-email-sign-up/', VerifyEmailSignUpView.as_view(), name='verify email initial'),
    path('verify-email-sign-in/<pk>', verify_email_sign_in_view, name='verify email additional'),
    path('activate-email/<pk>/<token>/', activate_email_view, name='activate email'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset password'),
    path('reset-password/sent/', UserPasswordResetDoneView.as_view(), name='reset password sent'),
    path('reset-password/confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='reset password confirm'),
    path('reset-password/complete/', UserPasswordResetCompleteView.as_view(), name='reset password complete'),
    path('sign-in-required/', RequireSignInView.as_view(), name='require sign in'),
]