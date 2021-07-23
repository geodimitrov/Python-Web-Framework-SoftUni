from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from book_center.bc_auth.models import BookCenterUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = BookCenterUser
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    pass
    # username = forms.CharField(
    #     max_length=20,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Enter your username'
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     max_length=20,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'placeholder': 'Enter your password'
    #         }
    #     ),
    # )

    # bots_catcher = forms.CharField(
    #     widget=forms.HiddenInput(),
    #     required=False,
    #     validators=[
    #         bot_catcher,
    #     ]
    # )
