from book_center.utils.validators import validate_alphabet_characters_english
from django.db import models


# class BookCenterBook(models.Model):
#     title = models.CharField(
#         max_length=100,
#         validators=(
#             validate_alphabet_characters_english,
#         )
#     )
#
#     author = models.CharField(
#         max_length=50,
#         validators=(
#             validate_alphabet_characters_english,
#         )
#     )
#
#     image = models.ImageField(
#         upload_to='books'
#     )
#
#     pages = models.PositiveIntegerField()
#
#     genre = models.CharField(
#         max_length=30,
#         blank=True,
#         validators=(
#             validate_alphabet_characters_english,
#         )
#     )
#
