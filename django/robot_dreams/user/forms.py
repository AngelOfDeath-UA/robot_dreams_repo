from django import forms
from . import models


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = models.User
        fields = ('first_name', 'age',)
