from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class BlogPostAuthorModelTests(BookCenterTestCase):

    def test_blog_post_author_model_when_first_name_contains_non_english_chars__expect_exception(self):
        self.blog_post_author.first_name = 'Бълхичкo'

        with self.assertRaises(ValidationError) as context:
            self.blog_post_author.full_clean()
            self.blog_post_author.save()

        self.assertIsNotNone(context.exception)

    def test_blog_post_author_model_when_last_name_contains_non_english_chars__expect_exception(self):
        self.blog_post_author.last_name = 'Хлебарков'

        with self.assertRaises(ValidationError) as context:
            self.blog_post_author.full_clean()
            self.blog_post_author.save()
        self.assertIsNotNone(context.exception)