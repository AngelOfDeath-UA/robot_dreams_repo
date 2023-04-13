from django.http import HttpResponse
from django.core import serializers
from .models import User
import json

def users(request):
    users = User.objects.all()
    users_json = json.loads(serializers.serialize('json', users))
    return HttpResponse(users_json)
