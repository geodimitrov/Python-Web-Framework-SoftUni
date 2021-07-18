from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/sign_up.html', context)


def sign_in_view(request):
    if request.method == 'POST':
        pass

    form = SignInForm()
    return render(request, 'auth/sign_in.html')


def sign_out_view(request):
    logout(request)
    return redirect('home')
