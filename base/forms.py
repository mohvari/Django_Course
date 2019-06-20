
from django import forms
from django.core.exceptions import ValidationError

from base.models import Member

#
# class SignupForm(forms.Form):
#     name = forms.CharField(max_length=128)
#     price = forms.IntegerField()
#     type = forms.CharField(max_length=128)


class SignupForm(forms.ModelForm):
    agreement = forms.BooleanField(required=False)

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean_agreement(self):
        if not self.cleaned_data.get('agreement'):
            raise ValidationError("You have to do that!")
