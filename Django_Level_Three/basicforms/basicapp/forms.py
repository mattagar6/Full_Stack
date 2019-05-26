from django import forms
# get built-in django validators
from django.core import validators

# custom validators ->django needs the parameter to be called 'value'
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with z')

class FormName(forms.Form):

    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again')
    text = forms.CharField(widget = forms.Textarea)

    # HIDDEN FIELDS -> bots inspect the page and change html form value keys directly
    # a human won't see the hidden field and won't fill in a value for it, but a bot will
    botcatcher = forms.CharField(required = False,
                                widget = forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)])
                                
    # cleans the entire form at once
    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        verify_email = all_clean['verify_email']

        if email != verify_email:
            raise forms.ValidationError('Make sure your emails match.')

    # the following method syntax is required by django -> def clean_fieldName(self):
    # does the same thing as the validator on the lines above
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        # if a bot scraped the page and filled in the value for botcatcher directly
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT')

        return botcatcher
