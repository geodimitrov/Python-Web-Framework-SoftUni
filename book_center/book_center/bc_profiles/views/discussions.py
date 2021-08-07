from book_center.bc_profiles.models.discussions import BookCenterDiscussion, BookCenterDiscussionComment, BookCenterDiscussionLike
from book_center.bc_profiles.forms.discussions import DiscussionForm, DiscussionCommentForm
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View


def save_comment(form, discussion, user):
    comment = form.save(commit=False)
    comment.discussion = discussion
    comment.author = user
    comment.save()


class AllDiscussionsView(LoginRequiredMixin, ListView):
    template_name = 'profiles/discussions/discussions.html'
    context_object_name = 'discussions'
    model = BookCenterDiscussion


@login_required()
def discussion_details_view(request, pk):
    discussion = get_object_or_404(BookCenterDiscussion, pk=pk)
    comments = BookCenterDiscussionComment.objects.filter(discussion=pk)
    is_liked_by_user = discussion.discussionlike_set.filter(user_id=request.user.id).exists()

    if request.method == 'POST':
        comment_form = DiscussionCommentForm(request.POST)

        if comment_form.is_valid():
            save_comment(comment_form, discussion, request.user)
            return redirect('discussion details', discussion.id)

    context = {
        'discussion': discussion,
        'comment': DiscussionCommentForm(),
        'all_comments': comments,
        'is_liked': is_liked_by_user,
    }
    return render(request, 'profiles/discussions/discussion_details.html', context)


class CreateDiscussionView(LoginRequiredMixin, CreateView):
    template_name = 'profiles/discussions/create_discussion.html'
    model = BookCenterDiscussion
    form_class = DiscussionForm
    success_url = reverse_lazy('show all discussions')

    def form_valid(self, form):
        discussion = form.save(commit=False)
        discussion.author = self.request.user
        discussion.save()
        return super().form_valid(form)


class EditDiscussionView(LoginRequiredMixin, UpdateView):
    template_name = 'profiles/discussions/edit_discussion.html'
    model = BookCenterDiscussion
    form_class = DiscussionForm
    success_url = reverse_lazy('show all discussions')


class DeleteDiscussionView(LoginRequiredMixin, DeleteView):
    template_name = 'profiles/discussions/delete_discussion.html'
    model = BookCenterDiscussion
    success_url = reverse_lazy('show all discussions')


class LikeCommentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        discussion = BookCenterDiscussion.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = discussion.discussionlike_set.filter(user_id=self.request.user.id).first()

        if not like_object_by_user:
            like = BookCenterDiscussionLike(
                discussion=discussion,
                user=self.request.user,
            )
            like.save()

        return redirect('discussion details', discussion.id)


@login_required()
def delete_comment_view(request, pk, comment_id):
    comment = BookCenterDiscussionComment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('discussion details', pk)

