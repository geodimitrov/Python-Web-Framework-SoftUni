from book_center.utils.validators import validate_alphabet_characters_english
from django.db import models


class BookCenterBlogPostAuthor(models.Model):
    first_name = models.CharField(
        max_length=20,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    last_name = models.CharField(
        max_length=20,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    class Meta:
        verbose_name = 'Author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BookCenterBlogPost(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )
    text = models.TextField(
        max_length=500,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    slug = models.SlugField(
        unique=True,
        validators=(
            validate_alphabet_characters_english,
        )
    )

    date_created = models.DateField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        BookCenterBlogPostAuthor,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Blog Post'
