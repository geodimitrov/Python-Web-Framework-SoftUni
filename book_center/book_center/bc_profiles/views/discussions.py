from book_center.bc_profiles.forms.discussions import BookCenterDiscussionForm
from book_center.bc_profiles.models.discussions import BookCenterDiscussion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required()
def discussions_view(request):
    context = {
        'form': BookCenterDiscussionForm(),
        'discussions': BookCenterDiscussion.objects.all()
    }
    return render(request, 'profiles/discussions/discussions.html', context)


@login_required()
def discussion_details_view(request, pk):
    discussion = BookCenterDiscussion.objects.get(pk=pk)
    context = {
        'discussion': discussion,
    }
    return render(request, 'profiles/discussions/discussion_details.html', context)