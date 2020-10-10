from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Storage


def index(request):
    head = 'Список складов' + '\r\n\r\n'
    for storage in Storage.objects.all():
        head += storage.storage_name + '\r\n' + 'Описание: ' + storage.storage_description + '\r\n\r\n'
        # later will add output information
    return HttpResponse(head, content_type='text/plain; charset=utf-8')
