from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.apps import apps


class MainView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'ziponline/index.html')
