from book_center.utils.mixins import NoLabelFormMixin
from book_center.utils.validators import validate_bot_catcher_empty
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms


class UserPasswordResetForm(NoLabelFormMixin, PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter your email address'
            }
        )
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        validate_bot_catcher_empty(self.cleaned_data['bots_catcher'])


class UserNewPasswordSetForm(NoLabelFormMixin, SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    new_password1 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password'}
        ),
    )

    new_password2 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your new password'}
        ),
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        validate_bot_catcher_empty(self.cleaned_data['bots_catcher'])
