from book_center.utils.validators import validate_alphabet_characters_english
from django.core.validators import MinLengthValidator
from django.db import models


class ContactFormModel(models.Model):
    class Meta:
        verbose_name = 'Contact Form'

    subject = models.CharField(
        max_length=50,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    email = models.EmailField(
        max_length=50,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    message = models.CharField(
        max_length=500,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(10),
        )
    )

    date_received = models.DateField(
        auto_now_add=True,
    )

    reply = models.BooleanField(
        default=False,
    )

from book_center.utils.signals import *