from django.http import HttpResponse
from django.core import serializers
from .models import Purchase
import json

def purchases(request):
    purchases = Purchase.objects.all()
    purchases_json = json.loads(serializers.serialize('json', purchases))
    return HttpResponse(purchases_json)

