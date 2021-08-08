from django.core.mail import send_mail
from django.test import TestCase

from book_center.utils.utils import send_confirmation_email


class SendConfirmationEmailTest(TestCase):

    def test(self):
        recipient_email = None
        expected_subject = 'Message Received'
        expected_message = 'Thank you for contacting us. We have received your message.'
        expected_sender_email = 'book_center_notifications@protonmail.com'
        result = send_confirmation_email(recipient_email)
        self.assertEqual(result['recipient_email'], 'So')
