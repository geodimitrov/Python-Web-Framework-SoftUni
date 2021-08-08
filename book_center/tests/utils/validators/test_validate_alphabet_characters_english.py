from book_center.utils.validators import validate_alphabet_characters_english
from django.core.exceptions import ValidationError
from django.test import TestCase


class ValidateAlphabetCharactersEnglishTests(TestCase):
    def test_when_contains_non_english_character__expect_exception(self):
        value = 'BabyБой'
        expected_validation_error_message = 'You are not allowed to use non-English characters'

        with self.assertRaises(ValidationError) as context:
             validate_alphabet_characters_english(value)

        self.assertEquals(expected_validation_error_message, context.exception.message)

    def test_when_does_not_contain_non_english_character__expect_execution(self):
        value = 'BabyBoy'
        validate_alphabet_characters_english(value)