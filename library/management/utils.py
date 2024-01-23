from django.shortcuts import get_object_or_404
from .models import *

def url_to_object(url):
    url = url.split("api/")[1].split('/')
    klass, pk, _ = url
    klass = eval(klass[0].upper() + klass[1:-1])
    return klass.objects.get(pk=pk)