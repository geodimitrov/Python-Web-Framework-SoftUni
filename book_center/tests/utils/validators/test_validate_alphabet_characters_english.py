from django.test import TestCase


class ValidateAlphabetCharactersEnglishTests(TestCase):
    pass

        # def test_when_bot_detected_expect_exception(self):
        #     value = 'bot'
        #     expected_validation_error_message = 'Bot detected'
        #
        #     with self.assertRaises(ValidationError) as context:
        #         validate_bot_catcher_empty(value)
        #
        #     self.assertEquals(expected_validation_error_message, context.exception.message)
        #
        # def test_when_no_bot_detected_expect_execution(self):
        #     value = ''
        #     validate_bot_catcher_empty(value)