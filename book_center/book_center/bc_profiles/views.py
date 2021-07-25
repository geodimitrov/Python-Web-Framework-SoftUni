from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from book_center.bc_auth.models import BookCenterUser
from book_center.bc_profiles.forms import UserProfileForm
from book_center.bc_profiles.models import BookCenterUserProfile


class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = BookCenterUser
    form_class = UserProfileForm
    success_url = reverse_lazy('home')


def show_all_profiles(request):
    context = {
        'profiles': BookCenterUserProfile.objects.all()
    }
    return render(request, 'profiles/all_profiles.html', context)
