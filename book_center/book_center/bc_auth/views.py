from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from book_center.bc_auth.forms import SignInForm, SignUpForm
from book_center.bc_auth.models import BookCenterUser


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = BookCenterUser
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(LogoutView):
    template_name = 'main/home.html'
    next_page = 'home'
