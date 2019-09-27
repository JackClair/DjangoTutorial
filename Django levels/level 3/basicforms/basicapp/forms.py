from django import forms
from django.core import validators

#def checkForZ(value):
    #if value[0].lower() != 'z':
    #    raise forms.ValidationError("Name Nedd to Start With Z only.")

class formName(forms.Form):
    #name = forms.CharField(max_length=100, validators=[checkForZ,])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    #botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
