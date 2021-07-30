from book_center.bc_auth.models import BookCenterUser
from book_center.utils.validators import validate_alphabet_characters_english
from django.db import models

SUPPORTED_COUNTRIES = [
    ('BG', 'Bulgaria'),
    ('UK', 'United Kingdom'),
    ('RO', 'Romania'),
]


class BookCenterUserProfile(models.Model):
    class Meta:
        verbose_name = 'Profile'

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

    profile_image = models.ImageField(
        upload_to='profiles',
        default='profiles/default_profile_img.jpg'
    )

    country = models.CharField(
        max_length=100,
        choices=SUPPORTED_COUNTRIES,
        blank=True,
    )

    user = models.OneToOneField(BookCenterUser, on_delete=models.CASCADE)