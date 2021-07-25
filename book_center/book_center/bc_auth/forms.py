from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from book_center.bc_auth.models import BookCenterUser
from book_center.utils.mixins import NoLabelFormMixin
from book_center.utils.validators import validate_bot_catcher_empty


class SignUpForm(UserCreationForm, NoLabelFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = BookCenterUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email*'}),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password*'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm your password*'}
        )
    )


class SignInForm(AuthenticationForm, NoLabelFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter your username'}
        )
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter your password'}
        ),
    )

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        validate_bot_catcher_empty(self.cleaned_data['bots_catcher'])