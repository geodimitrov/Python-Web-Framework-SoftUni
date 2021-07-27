from django.core.exceptions import ValidationError
import string


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('Bot detected')


def validate_alphabet_characters_english(value):
    for char in value.lower():
        if char.isalpha() and char not in string.ascii_lowercase:
            raise ValidationError('You are not allowed to use non-English characters')