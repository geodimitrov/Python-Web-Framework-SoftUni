from tests.core.test_cases import BookCenterTestCase
from django.core.exceptions import ValidationError


class UserModelTests(BookCenterTestCase):
    def test_user_model_when_username_contains_non_english_chars__expect_exception(self):
        self.user.username = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.user.full_clean()
            self.user.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_email_contains_non_english_chars__expect_exception(self):
        self.user.email = 'gъл@хичка.com'

        with self.assertRaises(ValidationError) as context:
            self.user.full_clean()
            self.user.save()

        self.assertIsNotNone(context.exception)
