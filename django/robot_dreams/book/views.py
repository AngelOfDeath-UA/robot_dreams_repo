from django.http import HttpResponse
from django.core import serializers
import json
from .models import Book

def books(request):
    book = Book.objects.all()
    book_json = json.loads(serializers.serialize('json', book))
    return HttpResponse(book_json)

