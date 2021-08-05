from book_center.bc_profiles.models.discussions import BookCenterDiscussion
from book_center.utils.mixins import DisableAutocompleteMixin
from django import forms


class BookCenterDiscussionForm(DisableAutocompleteMixin, forms.ModelForm):
    class Meta:
        model = BookCenterDiscussion
        fields = '__all__'