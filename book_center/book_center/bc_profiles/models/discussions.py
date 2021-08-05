from book_center.bc_auth.models import BookCenterUser
from book_center.utils.validators import validate_alphabet_characters_english
from django.core.validators import MinLengthValidator
from django.db import models

DISCUSSION_RATINGS = [
    ('1', 'Very interesting'),
    ('2', 'Interesting'),
    ('3', 'Cannot tell'),
    ('4', 'Somewhat boring'),
    ('5', 'Very boring'),
]


class BookCenterDiscussion(models.Model):
    title = models.CharField(
        max_length=50,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    description = models.CharField(
        max_length=200,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(10),
        )
    )

    topic = models.CharField(
        max_length=20,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    author = models.ForeignKey(
        BookCenterUser,
        on_delete=models.CASCADE
    )


class DiscussionComment(models.Model):
    comment = models.CharField(
        max_length=500,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    discussion = models.OneToOneField(
        BookCenterDiscussion,
        on_delete=models.CASCADE
    )

    author = models.OneToOneField(
        BookCenterUser,
        on_delete=models.CASCADE
    )

    like = models.BooleanField()
    dislike = models.BooleanField()

