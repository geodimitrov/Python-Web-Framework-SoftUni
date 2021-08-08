from book_center.bc_profiles.forms.discussions import DiscussionForm
from django.test import TestCase


class DiscussionFormTests(TestCase):
    # Test autocomplete
    def test_discussion_form_title_autocomplete__expect_off(self):
        expected_value = 'off'
        form = DiscussionForm()
        self.assertEqual(expected_value, form.fields['title'].widget.attrs['autocomplete'])

    def test_discussion_form_description_autocomplete__expect_off(self):
        expected_value = 'off'
        form = DiscussionForm()
        self.assertEqual(expected_value, form.fields['description'].widget.attrs['autocomplete'])

    def test_discussion_form_topic_autocomplete__expect_off(self):
        expected_value = 'off'
        form = DiscussionForm()
        self.assertEqual(expected_value, form.fields['topic'].widget.attrs['autocomplete'])

    # Test created_on for readonly
    def test_discussion_form_created_on_readonly__expect_readonly(self):
        expected_value = 'readonly'
        form = DiscussionForm()
        self.assertEqual(expected_value, form.fields['created_on'].widget.attrs['readonly'])
