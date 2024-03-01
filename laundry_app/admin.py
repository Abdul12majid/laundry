from django.contrib import admin
from .models import Order, ClotheType, Service, Action



# Register your models here.
admin.site.register(Order)
admin.site.register(ClotheType)
admin.site.register(Service)
admin.site.register(Action)
