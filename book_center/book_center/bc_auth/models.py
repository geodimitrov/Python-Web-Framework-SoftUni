from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

UserModel = settings.AUTH_USER_MODEL
# UserModel = get_user_model()


# Create a user profile
class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(
        max_length=20,
    )
    # profile_image = models.ImageField(
    #     upload_to=''
    # )
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)


# Create a custom user model
class BookCenterUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True
    )
    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'
