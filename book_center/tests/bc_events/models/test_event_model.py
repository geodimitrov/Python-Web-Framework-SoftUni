from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class EventModelTests(BookCenterTestCase):
    def test_event_model_when_title_contains_non_english_chars__expect_exception(self):
        self.event.title = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.event.full_clean()
            self.event.save()

        self.assertIsNotNone(context.exception)

    def test_event_model_when_description_contains_non_english_chars__expect_exception(self):
        self.event.description = 'Това е просто описание'

        with self.assertRaises(ValidationError) as context:
            self.event.full_clean()
            self.event.save()

        self.assertIsNotNone(context.exception)

    def test_event_model_when_category_contains_non_english_chars__expect_exception(self):
        self.event.category = 'CaterorЯ'

        with self.assertRaises(ValidationError) as context:
            self.event.full_clean()
            self.event.save()

        self.assertIsNotNone(context.exception)
