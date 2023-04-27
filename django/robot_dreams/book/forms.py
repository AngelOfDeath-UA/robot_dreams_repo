from django import forms
from . import models


class BookCreationForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    year = forms.IntegerField()
    price = forms.FloatField()

    class Meta:
        model = models.Book
        fields = ('title', 'author', 'year', 'price')
