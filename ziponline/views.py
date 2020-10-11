from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Storage, Warehouse


def index(request):
    storage = Storage.objects.order_by('storage_name')
    return render(request, 'ziponline/index.html', {'storage': storage})


def by_storage(request, storage_id):
    warehouses = Warehouse.objects.filter(storage=storage_id)  # returns ONE result if FILTER
    storages = Storage.objects.order_by('storage_name')
    current_storage = Storage.objects.get(pk=storage_id)      # returns MANY results if GET
    context = {'warehouses': warehouses, 'storages': storages, 'current_storage': current_storage}
    return render(request, 'ziponline/by_storage.html', context)
