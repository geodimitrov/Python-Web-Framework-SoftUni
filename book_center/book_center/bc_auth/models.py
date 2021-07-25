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
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'username'
    objects = BookCenterUserManager()