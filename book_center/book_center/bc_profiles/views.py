from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from book_center.bc_auth.models import BookCenterUser
from book_center.bc_profiles.forms import UserProfileForm
from book_center.bc_profiles.models import BookCenterUserProfile


@login_required()
def profile_main_view(request, username):
    return render(request, 'profiles/index.html')


@login_required()
def profile_details_view(request, username):
    user = BookCenterUser.objects.get(username=username)
    profile = BookCenterUserProfile.objects.get(pk=user.id)
    form = UserProfileForm(instance=profile)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile main', username)

    context = {
        'form': form,
    }
    return render(request, 'profiles/profile_details.html', context)


@login_required()
def edit_profile_view(request):
    return render(request, 'profiles/index.html')



