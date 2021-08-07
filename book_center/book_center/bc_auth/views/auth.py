from book_center.bc_auth.forms.auth import SignInForm, SignUpForm
from book_center.bc_auth.models import BookCenterUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect


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
            return redirect('profile main', user.username)
        else:
            return redirect('verify email additional', user.id)


class SignOutView(LogoutView):
    template_name = 'main/home.html'
    next_page = 'home'


class RequireSignInView(TemplateView):
    template_name = 'auth/require_sign_in.html'
