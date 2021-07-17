from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=50,
    )
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.Textarea()