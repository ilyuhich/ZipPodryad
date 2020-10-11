from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Storage, Warehouse, Moving
from .forms import MvForm


class MvCreateView(CreateView):
    template_name = 'ziponline/mv_create.html'
    form_class = MvForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movings'] = Moving.objects.all()
        return context


def index(request):
    storage = Storage.objects.order_by('storage_name')
    storages = Storage.objects.order_by('storage_name')
    return render(request, 'ziponline/index.html', {'storage': storage, 'storages': storages})


def by_storage(request, storage_id):
    warehouses = Warehouse.objects.filter(storage=storage_id)  # returns ONE result if FILTER
    storages = Storage.objects.order_by('storage_name')
    current_storage = Storage.objects.get(pk=storage_id)  # returns MANY results if GET
    context = {'warehouses': warehouses, 'storages': storages, 'current_storage': current_storage}
    return render(request, 'ziponline/by_storage.html', context)
