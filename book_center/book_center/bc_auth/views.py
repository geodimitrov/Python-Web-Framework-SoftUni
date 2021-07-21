from django.contrib.auth import logout, authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from book_center.bc_auth.forms import SignInForm, SignUpForm


def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign_up.html', context)


def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user:
                login(request, user)
                return redirect('home')

    form = SignInForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign_in.html', context)

    # user = authenticate(username='geo100', password='100')
    # login(request, user)
    # return redirect('home')


def sign_out_view(request):
    logout(request)
    return redirect('home')
