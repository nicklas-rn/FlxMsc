from django import forms

class ContactForm(forms.Form):
    contact_subject = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_subject'].label = "Subject"
        self.fields['contact_email'].label = "Your email address"
        self.fields['contact_content'].label = "Your message"