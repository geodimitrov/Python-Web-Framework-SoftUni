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
        on_delete=models.CASCADE,
        null=True
    )


class DiscussionComment(models.Model):
    body = models.CharField(
        max_length=500,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    discussion = models.ForeignKey(
        BookCenterDiscussion,
        on_delete=models.CASCADE,
        null=True
    )

    author = models.ForeignKey(
        BookCenterUser,
        on_delete=models.CASCADE,
        null=True
    )

    like = models.BooleanField(
        default=False
    )
    dislike = models.BooleanField(
        default=False
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']
