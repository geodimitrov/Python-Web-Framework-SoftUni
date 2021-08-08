from django.core.exceptions import ValidationError
from tests.core.test_cases import BookCenterTestCase


class ContactFormModelTests(BookCenterTestCase):
    def test_contact_form_model_when_subject_contains_non_english_chars__expect_exception(self):
        self.contact_form.subject = 'Бълхичка'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_email_contains_non_english_chars__expect_exception(self):
        self.contact_form.email = 'gъл@хичка.com'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

    def test_user_model_when_message_contains_non_english_chars__expect_exception(self):
        self.contact_form.message = 'Винаги съм искал да се свържа с вас'

        with self.assertRaises(ValidationError) as context:
            self.contact_form.full_clean()
            self.contact_form.save()

        self.assertIsNotNone(context.exception)

