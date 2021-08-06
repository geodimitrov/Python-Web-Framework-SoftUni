from book_center.bc_profiles.forms.discussions import BookCenterDiscussionForm, DiscussionCommentForm
from book_center.bc_profiles.models.discussions import BookCenterDiscussion, DiscussionComment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


def save_comment(form, discussion, user):
    comment = form.save(commit=False)
    comment.discussion = discussion
    comment.author = user
    comment.save()


@login_required()
def discussions_all_view(request):
    context = {
        'form': BookCenterDiscussionForm(),
        'discussions': BookCenterDiscussion.objects.all()
    }
    return render(request, 'profiles/discussions/discussions.html', context)


@login_required()
def discussion_details_view(request, pk):
    discussion = get_object_or_404(BookCenterDiscussion, pk=pk)
    comments = DiscussionComment.objects.filter(discussion=pk)

    if request.method == 'POST':
        comment_form = DiscussionCommentForm(request.POST)

        if comment_form.is_valid():
            save_comment(comment_form, discussion, request.user)
            return redirect('discussion details', discussion.id)

    context = {
        'discussion': discussion,
        'comment': DiscussionCommentForm(),
        'all_comments': comments,
    }
    return render(request, 'profiles/discussions/discussion_details.html', context)


@login_required()
def create_discussion_view(request):
    if request.method == 'POST':
        form = BookCenterDiscussionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show all discussions')

    context = {
        'form': BookCenterDiscussionForm(),
    }
    return render(request, 'profiles/discussions/create_discussion.html', context)


@login_required()
def edit_discussion_view(request, pk):
    discussion = BookCenterDiscussion.objects.get(pk=pk)
    if request.method == "POST":
        form = BookCenterDiscussionForm(request.POST, instance=discussion)

        if form.is_valid():
            form.save()
            return redirect('discussion details', discussion.id)

    context = {
        'form': BookCenterDiscussionForm(instance=discussion)
    }
    return render(request, 'profiles/discussions/edit_discussion.html', context)
