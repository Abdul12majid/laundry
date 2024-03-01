from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('settings', views.settings, name='settings'),

    path('index', views.index, name='index'),

    path('order', views.order, name='order'),

    path('save_data', views.save_data, name='save-data'),

    path('all_order', views.all_dashboard, name='all-orders'),
    path('paid_order', views.paid_dashboard, name='paid-orders'),    
    path('unpaid_order', views.unpaid_dashboard, name='unpaid-orders'),    
    path('view_order/<int:pk>', views.see_order, name='view-order'),    


    
]
