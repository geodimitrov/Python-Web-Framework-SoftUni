from book_center.bc_auth.models import BookCenterUser
from book_center.utils.validators import validate_alphabet_characters_english
from django.core.validators import MinLengthValidator
from django.db import models


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

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Discussion'

    def __str__(self):
        return self.title


class BookCenterDiscussionComment(models.Model):
    comment = models.CharField(
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
        verbose_name = 'Comment'


class BookCenterDiscussionLike(models.Model):
    discussion = models.ForeignKey(
        BookCenterDiscussion,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        BookCenterUser,
        on_delete=models.CASCADE
    )


class CommentUpvote(models.Model):
    comment = models.ForeignKey(
        BookCenterDiscussionComment,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        BookCenterUser,
        on_delete=models.CASCADE
    )