from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from book_center.utils.mixins import DisableAutocompleteMixin, NoLabelFormMixin
from book_center.utils.validators import validate_alphabet_characters_english
from django.contrib.auth.forms import PasswordChangeForm
from django.core.validators import MinLengthValidator
from django import forms


class UserProfileForm(DisableAutocompleteMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = BookCenterUserProfile
        exclude = ('user', )

    bio = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tell us a few words about yourself',

            }
        )
    )


class ChangePasswordForm(NoLabelFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    old_password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your current password*'}
        ),
    )

    new_password1 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your new password*'}
        ),
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5)
        )
    )

    new_password2 = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your new password*'}
        ),
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5)
        )
    )
