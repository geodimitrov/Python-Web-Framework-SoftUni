from django import forms
from book_center.bc_events.models import BookCenterEvent


class BookCenterEventForm(forms.ModelForm):
    class Meta:
        model = BookCenterEvent
        fields = '__all__'

    description = forms.CharField(
        max_length=200,
        widget=forms.Textarea(),
    )
