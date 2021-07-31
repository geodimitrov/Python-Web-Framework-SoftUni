from django.shortcuts import render
from book_center.bc_auth.models import BookCenterUser
from book_center.bc_profiles.forms import UserProfileForm
from book_center.bc_profiles.models import BookCenterUserProfile


def profile_main_view(request, username):
    user = BookCenterUser.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request, 'profiles/index.html', context)


def profile_details_view(request, username):
    user = BookCenterUser.objects.get(username=username)
    profile = BookCenterUserProfile.objects.get(pk=user.id)
    form = UserProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profiles/profile_details.html', context)


def edit_profile_view(request):
    return render(request, 'profiles/index.html')



