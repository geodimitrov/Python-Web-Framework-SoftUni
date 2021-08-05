from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_confirmation_email(recipient_email):
    subject = 'Message Received'
    message = 'Thank you for contacting us. We have received your message.'
    sender_email = 'book_center_notifications@protonmail.com'
    return send_mail(subject, message, sender_email, [recipient_email])


def send_verification_email(recipient_email, context):
    subject = 'Verify Your Email Address'
    message = render_to_string('auth/email_verification/verify_email_msg.html', context)
    sender_email = 'book_center_notifications@protonmail.com'
    return send_mail(subject, message, sender_email, [recipient_email])