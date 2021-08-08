from book_center.bc_auth.forms.auth import SignInForm
from django.test import TestCase


class SignInFormTests(TestCase):

    # Test labels
    def test_sign_in_form_username_label__expect_empty_label(self):
        expected_label = ''
        form = SignInForm()
        self.assertEqual(expected_label, form['username'].label)

    def test_sign_in_form_password_label__expect_empty_label(self):
        expected_label = ''
        form = SignInForm()
        self.assertEqual(expected_label, form['password'].label)

    # Test placeholders
    def test_sign_ip_form_username_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your username'
        form = SignInForm()
        self.assertEqual(expected_placeholder, form.fields['username'].widget.attrs['placeholder'])

    def test_sign_in_form_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your password'
        form = SignInForm()
        self.assertEqual(expected_placeholder, form.fields['password'].widget.attrs['placeholder'])