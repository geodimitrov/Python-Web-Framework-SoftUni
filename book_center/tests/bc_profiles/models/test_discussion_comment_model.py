from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class DiscussionCommentModelTests(BookCenterTestCase):
    def test_discussion_model_when_title_contains_non_english_chars__expect_exception(self):
        self.discussion_comment.comment = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.discussion_comment.full_clean()
            self.discussion_comment.save()

        self.assertIsNotNone(context.exception)