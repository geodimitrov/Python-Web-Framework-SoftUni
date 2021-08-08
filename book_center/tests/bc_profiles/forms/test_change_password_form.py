from book_center.bc_profiles.forms.profiles import ChangePasswordForm
from django.test import TestCase


class ChangePasswordFormTests(TestCase):
    def setUp(self) -> None:
        self.data = {
            'user': 'geo100',
            'old_password': 'jhy',
            'new_password1': 'Baby87',
            'new_password2': 'Baby87',
        }

    # Test labels
    def test_change_password_form_old_password_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_label, form['old_password'].label)

    def test_change_password_form_new_password1_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_label, form['new_password1'].label)

    def test_change_password_form_new_password2_label__expect_empty_label(self):
        expected_label = ''
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_label, form['new_password2'].label)

    # Test placeholders
    def test_change_password_form_old_password_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your current password*'
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_placeholder, form.fields['old_password'].widget.attrs['placeholder'])

    def test_change_password_form_new_password1_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your new password*'
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_placeholder, form.fields['new_password1'].widget.attrs['placeholder'])

    def test_change_password_form_new_password2_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Confirm your new password*'
        form = ChangePasswordForm(self.data['user'])
        self.assertEqual(expected_placeholder, form.fields['new_password2'].widget.attrs['placeholder'])


