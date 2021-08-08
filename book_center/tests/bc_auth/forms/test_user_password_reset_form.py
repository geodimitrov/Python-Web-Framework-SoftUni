from book_center.bc_auth.forms.password_reset import UserPasswordResetForm
from django.test import TestCase


class UserPasswordResetFormTests(TestCase):
    def test_user_password_reset_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = UserPasswordResetForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_sign_up_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your email address'
        form = UserPasswordResetForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])