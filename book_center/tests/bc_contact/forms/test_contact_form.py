from book_center.bc_contact.forms import ContactForm
from django.test import TestCase


class ContactFormTests(TestCase):

    # Test labels
    def test_contact_form_subject_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['subject'].label)

    def test_contact_form_email_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['email'].label)

    def test_contact_form_message_label__expect_empty_label(self):
        expected_label = ''
        form = ContactForm()
        self.assertEqual(expected_label, form['message'].label)

    def test_contact_form_subject_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Subject'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['subject'].widget.attrs['placeholder'])

    def test_contact_form_email_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Email'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['email'].widget.attrs['placeholder'])

    def test_contact_form_message_placeholder__expect_correct_placeholder(self):
        expected_placeholder = 'Tell us what\'s on your mind'
        form = ContactForm()
        self.assertEqual(expected_placeholder, form.fields['message'].widget.attrs['placeholder'])

