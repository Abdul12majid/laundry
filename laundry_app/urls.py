from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('settings', views.settings, name='settings'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('index', views.index, name='index'),

    path('order', views.order, name='order'),
    path('process_order', views.processOrder, name='process-order'),

    path('save_data', views.save_data, name='save-data'),

    path('dynamic_data', views.dynamic_data, name='dynamic-data'),
    
]
