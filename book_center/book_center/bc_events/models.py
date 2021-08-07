from book_center.bc_auth.models import BookCenterUser
from book_center.utils.validators import validate_alphabet_characters_english
from django.db import models


EVENT_CATEGORIES = [
    ('book_month', 'Book of the Month'),
    ('book_fair', 'Book Fair'),
    ('author_meeting', 'Author Meeting'),
    ('public_reading', 'Public Reading'),
]


class BookCenterEvent(models.Model):
    title = models.CharField(
        max_length=100,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    description = models.CharField(
        max_length=200,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    is_book_of_month = models.BooleanField(
        default=False,
    )

    category = models.CharField(
        max_length=50,
        choices=EVENT_CATEGORIES,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    event_image = models.ImageField(
        upload_to='events',
    )

    event_date = models.DateField()

    class Meta:
        verbose_name = 'Event'

    def __str__(self):
        return self.title


class BookCenterEventRegister(models.Model):
    event = models.ForeignKey(
        BookCenterEvent,
        on_delete=models.CASCADE
    )

    registration_date = models.DateTimeField(
        auto_now_add=True
    )

    participant = models.OneToOneField(
        BookCenterUser,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Event Log'
