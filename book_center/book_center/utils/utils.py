from django.core.mail import send_mail


def send_confirmation_email(recipient_email):
    subject = 'Message Received'
    message = 'Thank you for contacting us. We have received your message. '
    sender_email = 'book_center_notifications@protonmail.com'
    return send_mail(subject, message, sender_email, [recipient_email])


