from book_center.bc_auth.forms import SignInForm, SignUpForm
from book_center.bc_auth.models import BookCenterUser
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse


class SignUpView(CreateView):
    template_name = 'auth/sign_up.html'
    model = BookCenterUser
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=self.request.POST['username'],
            password=self.request.POST['password1'],
        )
        login(self.request, user)
        return redirect('home')


class SignInView(LoginView):
    template_name = 'auth/sign_in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse('home')


class SignOutView(LogoutView):
    template_name = 'main/home.html'
    next_page = 'home'
