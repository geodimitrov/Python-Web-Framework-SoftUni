from book_center.bc_profiles.forms.profiles import UserProfileForm
from django.test import TestCase


class UserProfileFormTests(TestCase):
    pass

    # Test autocomplete
    def test_user_profile_form_first_name_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['first_name'].widget.attrs['autocomplete'])

    def test_user_profile_form_last_name_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['last_name'].widget.attrs['autocomplete'])

    def test_user_profile_form_bio_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['bio'].widget.attrs['autocomplete'])

    def test_user_profile_form_city_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['city'].widget.attrs['autocomplete'])

    def test_user_profile_form_twitter_account_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['twitter_account'].widget.attrs['autocomplete'])

    def test_user_profile_form_facebook_account_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['facebook_account'].widget.attrs['autocomplete'])

    def test_user_profile_form_instagram_account_autocomplete__expect_off(self):
        expected_value = 'off'
        form = UserProfileForm()
        self.assertEqual(expected_value, form.fields['instagram_account'].widget.attrs['autocomplete'])

    #Test bio for placeholder
    def test_user_profile_form_bio_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Tell us a few words about yourself'
        form = UserProfileForm()
        self.assertEqual(expected_placeholder, form.fields['bio'].widget.attrs['placeholder'])
