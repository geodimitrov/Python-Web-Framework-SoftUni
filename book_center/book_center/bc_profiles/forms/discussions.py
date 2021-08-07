from book_center.bc_profiles.models.discussions import BookCenterDiscussion, BookCenterDiscussionComment
from book_center.utils.mixins import DisableAutocompleteMixin
from django import forms


class DiscussionForm(DisableAutocompleteMixin, forms.ModelForm):
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

    created_on = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'readonly': 'readonly'
            }
        ),
        required=False,
    )


class DiscussionCommentForm(DisableAutocompleteMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = BookCenterDiscussionComment
        fields = ('comment', )

    comment = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Leave a comment',
                'rows': 3,
            }
        ),
    )

