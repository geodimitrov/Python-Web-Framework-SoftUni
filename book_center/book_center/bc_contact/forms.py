from book_center.bc_contact.models import ContactFormModel
from book_center.utils.validators import validate_bot_catcher_empty
from book_center.utils.mixins import NoLabelFormMixin
from django import forms


class ContactForm(NoLabelFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = ContactFormModel
        exclude = ('reply',)
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us what\'s on your mind', 'rows': 6})
        }

    bots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bots_catcher(self):
        validate_bot_catcher_empty(self.cleaned_data['bots_catcher'])
