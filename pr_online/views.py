from django.shortcuts import render
from django.views.generic.list import ListView
from .models import PRModel


# Create your views here.

class PRView(ListView):
    """вывод списка ПР в работе"""
    template_name = 'pr_online/pr_list.html'
    model = PRModel

