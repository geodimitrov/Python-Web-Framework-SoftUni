from django.db import models
from book_center.utils.validators import validate_alphabet_characters_english


class BlogPostAuthor(models.Model):
    class Meta:
        verbose_name = 'Author'

    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BlogPost(models.Model):
    class Meta:
        verbose_name = 'Blog Post'

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
    )

    date_created = models.DateField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        BlogPostAuthor,
        on_delete=models.CASCADE,
        default=1,
    )

