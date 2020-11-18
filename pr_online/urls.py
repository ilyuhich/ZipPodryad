from django.urls import path
from .views import PRView

urlpatterns = [
    path('', PRView.as_view(), name='PRView'),
]