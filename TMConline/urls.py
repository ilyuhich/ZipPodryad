from django.urls import path
from .views import TMCView

urlpatterns = [
    path('', TMCView.as_view(), name='TMCView'),
]