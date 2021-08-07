from book_center.utils.validators import validate_alphabet_characters_english
from django.core.validators import MinLengthValidator
from django.db import models


class BookCenterContactFormModel(models.Model):
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

    class Meta:
        verbose_name = 'Contact Form'


from book_center.utils.signals import *
