from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Storage)
admin.site.register(Good)
admin.site.register(Moving)
admin.site.register(Warehouse)
