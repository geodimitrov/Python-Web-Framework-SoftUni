from book_center.bc_auth.forms.password_reset import UserPasswordResetForm, UserNewPasswordSetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


class UserPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset/reset_password.html'
    from_email = 'book_center_notifications@protonmail.com'
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('reset password sent')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'auth/password_reset/reset_password_sent.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'auth/password_reset/reset_password_confirm.html'
    form_class = UserNewPasswordSetForm
    success_url = reverse_lazy('reset password complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'auth/password_reset/reset_password_complete.html'
