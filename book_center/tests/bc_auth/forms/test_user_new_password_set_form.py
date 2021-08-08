from django.test import TestCase

from book_center.bc_auth.forms.password_reset import UserNewPasswordSetForm


class UserNewPasswordSetFormTests(TestCase):

    def test_new_password_set_form_password1_label__expect_empty_label(self):
        expected_label = ''
        form = UserNewPasswordSetForm(user='geo')
        self.assertEqual(expected_label, form['new_password1'].label)

    def test_new_password_set_form_form_password2_label__expect_empty_label(self):
        expected_label = ''
        form = UserNewPasswordSetForm(user='geo')
        self.assertEqual(expected_label, form['new_password2'].label)

    def test_new_password_set_form_password1_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Enter your new password'
        form = UserNewPasswordSetForm(user='geo')
        self.assertEqual(expected_placeholder, form.fields['new_password1'].widget.attrs['placeholder'])

    def test_new_password_set_form_password2_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Confirm your new password'
        form = UserNewPasswordSetForm(user='geo')
        self.assertEqual(expected_placeholder, form.fields['new_password2'].widget.attrs['placeholder'])