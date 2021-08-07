from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from book_center.bc_contact.models import BookCenterContactFormModel
from book_center.utils.tokens import account_activation_token
from book_center.utils.utils import send_confirmation_email, send_verification_email
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


@receiver(post_save, sender=BookCenterContactFormModel)
def contact_form_submit(sender, instance, **kwargs):
    send_confirmation_email(instance.email)


@receiver(post_save, sender=User)
def new_user_sign_up(sender, instance, created, **kwargs):
    user = instance
    context = {
        'user': user,
        'domain': 'http://127.0.0.1:8000',
        'token': account_activation_token.make_token(user)
    }

    if created:
        send_verification_email(user.email, context)
        profile = BookCenterUserProfile(
            user=instance,
        )
        profile.save()