# this is the local urls file for app ziponline
# /moves - goods movings
# /warehouse - shows current status of goods on all warehouses


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
