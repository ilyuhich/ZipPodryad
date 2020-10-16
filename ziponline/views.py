from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Storage, Moving, Good, Sklad
from .forms import MvForm

import datetime


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


def wh_together(request):
    goods = Good.objects.order_by('goods_name')
    wh_all = Warehouse.objects.order_by('good')
    current_date = datetime.datetime.now()
    stor_all = Storage.objects.order_by('storage_name')
    wh1 = Warehouse.objects.filter(storage='1')
    context = {
        'wh_all': wh_all,
        'current_date': current_date,
        'stor_all': stor_all,
        'goods': goods,
        'wh1': wh1
    }
    return render(request, 'ziponline/wh_together.html', context)


def skl_all(request):
    skl_ordered_by_goods = Sklad.objects.order_by('-good')
    current_date = datetime.datetime.now()
    context = {
        'skl_ordered_by_goods': skl_ordered_by_goods,
        'current_date': current_date
    }
    return render(request, 'ziponline/skl_all.html', context)