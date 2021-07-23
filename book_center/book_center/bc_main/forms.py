from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject'
            }
        )
    )
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name'
            }
        )
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name'
            }
        )
    )
    email = forms.EmailField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email'
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    'placeholder': 'Tell us what you think'
            }
        )
    )