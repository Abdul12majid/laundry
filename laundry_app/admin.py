from django.contrib import admin
from .models import Order, ClotheType, Service, Pre_order, Action



# Register your models here.
admin.site.register(Order)
admin.site.register(ClotheType)
admin.site.register(Service)
admin.site.register(Pre_order)
admin.site.register(Action)
