from book_center.bc_auth.forms.auth import SignUpForm
from django.test import TestCase

class SignUpFormTests(TestCase):

    # Test labels
    def test_sign_up_form_username_label__expect_empty_label(self):
        expected_label = ''
        form = SignUpForm()
        self.assertEqual(expected_label, form['username'].label)

    def test_sign_up_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = SignUpForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_sign_up_form_password1_label__expect_empty_label(self):
        expected_label = ''
        form = SignUpForm()
        self.assertEqual(expected_label, form['password1'].label)

    def test_sign_up_form_password2_label__expect_empty_label(self):
        expected_label = ''
        form = SignUpForm()
        self.assertEqual(expected_label, form['password2'].label)

    # Test placeholders
    def test_sign_up_form_username_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your username*'
        form = SignUpForm()
        self.assertEqual(expected_placeholder, form.fields['username'].widget.attrs['placeholder'])

    def test_sign_up_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your email*'
        form = SignUpForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])

    def test_sign_up_form_password1_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your password*'
        form = SignUpForm()
        self.assertEqual(expected_placeholder, form.fields['password1'].widget.attrs['placeholder'])

    def test_sign_up_form_password2_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Confirm your password*'
        form = SignUpForm()
        self.assertEqual(expected_placeholder, form.fields['password2'].widget.attrs['placeholder'])
