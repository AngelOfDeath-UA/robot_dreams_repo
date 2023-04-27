from django import forms
from . import models
from user.models import User
from book.models import Book


class PurchaseCreationForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all())
    book_id = forms.ModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = models.Purchase
        fields = ('user_id', 'book_id',)
