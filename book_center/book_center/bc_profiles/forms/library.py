from book_center.bc_profiles.models.library import BookCenterBook
from django import forms


class BookCenterBookForm(forms.ModelForm):
    class Meta:
        model = BookCenterBook
        fields = "__all__"