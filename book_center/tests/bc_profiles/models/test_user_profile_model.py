from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class DiscussionModelTests(BookCenterTestCase):
    def test_user_profile_model_when_first_name_contains_non_english_chars__expect_exception(self):
        self.profile.first_name = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.profile.full_clean()
            self.profile.save()

        self.assertIsNotNone(context.exception)

    def test_user_profile_model_when_last_name_contains_non_english_chars__expect_exception(self):
        self.profile.last_name = 'Хлебарков'

        with self.assertRaises(ValidationError) as context:
            self.profile.full_clean()
            self.profile.save()

        self.assertIsNotNone(context.exception)

    def test_user_profile_model_when_bio_contains_non_english_chars__expect_exception(self):
        self.profile.bio = 'Моето готино био'

        with self.assertRaises(ValidationError) as context:
            self.profile.full_clean()
            self.profile.save()

        self.assertIsNotNone(context.exception)

    def test_user_profile_model_when_city_contains_non_english_chars__expect_exception(self):
        self.profile.city = 'SofiЯ'

        with self.assertRaises(ValidationError) as context:
            self.profile.full_clean()
            self.profile.save()

        self.assertIsNotNone(context.exception)