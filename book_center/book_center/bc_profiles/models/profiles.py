from book_center.bc_auth.models import BookCenterUser
from book_center.utils.validators import validate_alphabet_characters_english
from django.db import models

SUPPORTED_COUNTRIES = [
    ('BG', 'Bulgaria'),
    ('UK', 'United Kingdom'),
    ('RO', 'Romania'),
]


class BookCenterUserProfile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    last_name = models.CharField(
        max_length=20,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    bio = models.CharField(
        max_length=200,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        ),
    )

    profile_image = models.ImageField(
        upload_to='profiles',
        default='profiles/default_profile_img.jpg'
    )

    country = models.CharField(
        max_length=100,
        choices=SUPPORTED_COUNTRIES,
        blank=True,
    )

    city = models.CharField(
        max_length=50,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    twitter_account = models.CharField(
        max_length=50,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    facebook_account = models.CharField(
        max_length=50,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    instagram_account = models.CharField(
        max_length=50,
        blank=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    user = models.OneToOneField(BookCenterUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profile'
