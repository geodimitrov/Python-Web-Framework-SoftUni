from book_center.bc_profiles.forms.discussions import DiscussionCommentForm
from django.test import TestCase


class DiscussionCommentFormTests(TestCase):

    def test_discussion_comment_form_comment_autocomplete__expect_off(self):
        expected_value = 'off'
        form = DiscussionCommentForm()
        self.assertEqual(expected_value, form.fields['comment'].widget.attrs['autocomplete'])

    def test_discussion_comment_form_comment_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Leave a comment'
        form = DiscussionCommentForm()
        self.assertEqual(expected_placeholder, form.fields['comment'].widget.attrs['placeholder'])

    def test_discussion_comment_form_comment_rows__expect_correct_value(self):
        expected_rows = 3
        form = DiscussionCommentForm()
        self.assertEqual(expected_rows, form.fields['comment'].widget.attrs['rows'])

