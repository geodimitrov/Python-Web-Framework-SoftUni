from django import forms
from book_center.bc_profiles.models import BookCenterUserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = BookCenterUserProfile
        fields = '__all__'