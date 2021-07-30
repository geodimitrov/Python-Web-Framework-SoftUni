from django.contrib.auth import login
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from book_center.bc_auth.forms import SignInForm, SignUpForm
from book_center.bc_auth.models import BookCenterUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from book_center.utils.tokens import account_activation_token
from book_center.utils.utils import send_verification_email


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = BookCenterUser
    form_class = SignUpForm
    success_url = reverse_lazy('verify email initial')


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm

    def form_valid(self, form):
        user = form.get_user()
        if user.is_verified:
            login(self.request, user)
            return redirect('home')
        else:
            return redirect('verify email additional', user.id)


class SignOutView(LogoutView):
    template_name = 'main/home.html'
    next_page = 'home'


class VerifyEmailSignUpView(TemplateView):
    template_name = 'auth/verification/verify_email_initial.html'


class VerifyEmailSignInView(TemplateView):
    template_name = 'auth/verification/verify_email_additional.html'


def verify_email_sign_in_view(request, pk):
    user = BookCenterUser.objects.get(pk=pk)
    template_name = 'auth/verification/verify_email_additional.html'
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
