from django.db import models
from book_center.utils.validators import validate_alphabet_characters_english

EVENT_CATEGORIES = [
    ('book_month', 'Book of the Month'),
    ('book_fair', 'Book Fair'),
    ('author_meeting', 'Author Meeting'),
    ('public_reading', 'Public Reading'),
]


class BookCenterEvent(models.Model):
    class Meta:
        verbose_name = 'Event'

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
