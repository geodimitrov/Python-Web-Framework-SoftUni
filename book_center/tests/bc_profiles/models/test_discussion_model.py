from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class DiscussionModelTests(BookCenterTestCase):
    def test_discussion_model_when_title_contains_non_english_chars__expect_exception(self):
        self.discussion.title = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.discussion.full_clean()
            self.discussion.save()

        self.assertIsNotNone(context.exception)

    def test_discussion_model_when_description_contains_non_english_chars__expect_exception(self):
        self.discussion.description = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.discussion.full_clean()
            self.discussion.save()

        self.assertIsNotNone(context.exception)

    def test_discussion_model_when_topic_contains_non_english_chars__expect_exception(self):
        self.discussion.topic = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.discussion.full_clean()
            self.discussion.save()

        self.assertIsNotNone(context.exception)