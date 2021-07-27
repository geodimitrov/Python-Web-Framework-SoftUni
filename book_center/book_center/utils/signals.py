from django.db.models.signals import post_save
from django.dispatch import receiver
from book_center.bc_contact.models import ContactFormModel
from book_center.utils.utils import send_confirmation_email


@receiver(post_save, sender=ContactFormModel)
def contact_form_submit(sender, instance, **kwargs):
    send_confirmation_email(instance.email)