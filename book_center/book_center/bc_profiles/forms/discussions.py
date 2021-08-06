from book_center.bc_profiles.models.discussions import BookCenterDiscussion, DiscussionComment
from django import forms

from book_center.utils.mixins import DisableAutocompleteMixin


class BookCenterDiscussionForm(DisableAutocompleteMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = BookCenterDiscussion
        exclude = ('author',)

    description = forms.CharField(
        max_length=200,
        widget=forms.Textarea()
    )


class DiscussionCommentForm(DisableAutocompleteMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = DiscussionComment
        fields = ('body', )

    body = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Leave a comment',
                'rows': 3,
                'label': 'Comment'
            }
        ),
        required=False
    )
