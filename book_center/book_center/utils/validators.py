from django.core.exceptions import ValidationError


def validate_bot_catcher_empty(value):
    if value:
        raise ValidationError('A bot!')