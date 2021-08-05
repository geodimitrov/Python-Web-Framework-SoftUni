from book_center.bc_auth.models import BookCenterUser
from book_center.bc_profiles.models.profiles import BookCenterUserProfile
from book_center.bc_profiles.forms.profiles import ChangePasswordForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class ProfileMainView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/index.html'
    pk_url_kwarg = "username"


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'profiles/profiles/change_password.html'
    form_class = ChangePasswordForm
    pk_url_kwarg = "username"
    success_url = reverse_lazy('reset password complete')


@login_required()
def profile_details_view(request, username):
    user = BookCenterUser.objects.get(username=username)
    profile = BookCenterUserProfile.objects.get(user_id=user.id)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile main', username)

    context = {
        'form': form,
    }
    return render(request, 'profiles/profiles/profile_details.html', context)


@login_required()
def edit_profile_view(request):
    return render(request, 'profiles/index.html')
