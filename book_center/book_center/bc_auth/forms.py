from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()
# UserModel = settings.AUTH_USER_MODEL


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password1', 'password2']


class SignInForm(forms.Form):
    # username = forms.CharField(
    #     max_length=20,
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Enter your username'
    #         }
    #     )
    # )
    email = forms.EmailField()
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password'
            }
        ),
    )

    # bots_catcher = forms.CharField(
    #     widget=forms.HiddenInput(),
    #     required=False,
    #     validators=[
    #         bot_catcher,
    #     ]
    # )
