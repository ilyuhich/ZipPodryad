# this is the local urls file for app ziponline
# /moves - goods movings
# /warehouse - shows current status of goods on all warehouses


from django.urls import path
from .views import index, by_storage

urlpatterns = [
    path('', index, name='index'),
    path('<int:storage_id>/', by_storage, name='by_storage'),
]
