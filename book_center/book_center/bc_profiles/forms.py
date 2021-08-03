from django import forms
from book_center.bc_profiles.models import BookCenterUserProfile
from book_center.utils.mixins import DisableAutocompleteMixin


class UserProfileForm(DisableAutocompleteMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = BookCenterUserProfile
        fields = '__all__'

    bio = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Tell us a few words about yourself',

            }
        )
    )
    
