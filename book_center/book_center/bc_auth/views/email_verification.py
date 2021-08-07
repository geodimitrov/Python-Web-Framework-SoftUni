from book_center.bc_auth.models import BookCenterUser
from book_center.utils.tokens import account_activation_token
from book_center.utils.utils import send_verification_email
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError


class VerifyEmailSignUpView(TemplateView):
    template_name = 'auth/email_verification/verify_email_initial.html'


def verify_email_sign_in_view(request, pk):
    user = BookCenterUser.objects.get(pk=pk)
    template_name = 'auth/email_verification/verify_email_additional.html'
    context = {
        'user': user,
        'domain': 'http://127.0.0.1:8000',
        'token': account_activation_token.make_token(user)
    }
    send_verification_email(user.email, context)
    return render(request, template_name)


def activate_email_view(request, pk, token):
    try:
        user = BookCenterUser.objects.get(pk=pk)
    except:
        raise ValidationError('User does not exist')

    if user and account_activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        return redirect('sign in')
    else:
        return ValidationError('Activation link is invalid!')

