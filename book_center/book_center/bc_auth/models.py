from book_center.utils.validators import validate_alphabet_characters_english
from django.core.validators import MinLengthValidator
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin, UserManager
from django.db import models


class BookCenterUserManager(UserManager):
    pass


class BookCenterUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'

    username = models.CharField(
        max_length=20,
        unique=True,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'
    objects = BookCenterUserManager()