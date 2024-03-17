from django.shortcuts import render, redirect
from .models import ClotheType, Service, Order, Action
from django.views.decorators.csrf import csrf_protect
import json
from django.http import JsonResponse
from django.db.models import Sum
from bs4 import BeautifulSoup
from django.contrib import messages


# Create your views here.


def settings(request):
	return render(request, 'settings.html', )

def dashboard(request):
	return render(request, 'dashboard.html', )


def index(request):
  services = Service.objects.all()
  clothes = ClotheType.objects.all()
  return render(request, 'index.html', {'services':services, 'clothes':clothes})


def order(request):
	if request.method == 'POST':
		number = request.POST[0]
		#action = request.POST[]
		return render(request, 'receipt.html', {'number':number, 'action':action})
	return render(request, 'receipt.html', {})



l = []

import codecs

@csrf_protect
def save_data(request):
  if request.method == 'POST':
    data = json.loads(request.body.decode('utf-8'))

    content = data['content']
    order_id = data['xxx']
    price = data['total_price']
    clothes = data['total_clothes']
    services = "gggg"
    paid = data['pay']
    payment = str(paid)

    soup = BeautifulSoup(content, 'html.parser')
    clean_text = soup.get_text(separator='\n')
    cleaned_text_1 = clean_text.replace('Delete', '')  # Using string replace
    
    
    #encoded_content = clean_text.encode('utf-8')  # Assuming UTF-8 encoding
    x = cleaned_text_1.encode('ascii', 'ignore').decode()

    if payment == 'True':
      new_record = Order.objects.create(
        details=x, 
        order_id=order_id, 
        total_price=price, 
        paid=True,

        )
      new_record.save()
    else:
      new_record = Order.objects.create(
        details=x, 
        order_id=order_id, 
        total_price=price, 
        )
      new_record.save()

    
    return JsonResponse({'success': True})
  else:
    return JsonResponse({'error': 'Invalid request method'})



def get_total_price():
  total_price = Order.objects.aggregate(total_price=Sum('total_price'))['total_price']
  return total_price

def all_dashboard(request):
    # 1. All orders
    services = Service.objects.all()
    all_orders = Order.objects.all().order_by('-date_added')
    t_count = Order.objects.count()
    total_price = get_total_price()


    context = {
        'all_orders': all_orders,
        'services': services,
        
        't_count': t_count,
        
        'total_price': total_price,
    }

    return render(request, 'all_order.html', context)


def paid_dashboard(request):
    # 1. All orders
    
    services = Service.objects.all()
    total_price = Order.objects.filter(paid=True).aggregate(total_paid=Sum('total_price'))['total_paid'] or 0

    # 2. All paid orders
    all_orders = Order.objects.filter(paid=True).order_by('-date_added')
    t_count = all_orders.count()

    # 3. All unpaid orders (paid=False)
    

    context = {
        'all_orders': all_orders,
        'services': services,
        
        't_count': t_count,
        
        'total_price': total_price,
    }

    return render(request, 'paid_dashboard.html', context)


def unpaid_dashboard(request):
    # 1. All orders
    services = Service.objects.all()
    all_orders = Order.objects.filter(paid=False).order_by('-date_added')
    t_count = all_orders.count()
    total_price = Order.objects.filter(paid=False).aggregate(total_paid=Sum('total_price'))['total_paid'] or 0



    context = {
        'all_orders': all_orders,
        'services': services,

        't_count': t_count,

        'total_price': total_price,
    }

    return render(request, 'unpaid_dashboard.html', context)


def see_order(request, pk):
  order = Order.objects.get(id=pk)
  actions = Action.objects.all()
  if request.method == "POST":
    payment_status = request.POST['payment']
    order_status = request.POST['order_status']  # Use the new name
    order.paid = payment_status
    order.action = Action.objects.get(id=order_status)  # Use the actual ID
    order.save()
    messages.success(request, ('Order updated'))
  return render(request, 'view_order.html', {'order': order, 'actions': actions})


def update_order(request, pk):
  get_order = Order.objects.get(id=pk)
  actions  = Action.objects.all()
  return render(request, 'settings.html')



def delete_order(request, pk):
  get_order = Order.objects.get(id=pk)
  if request.user.is_superuser:
    get_order.delete()
    messages.success(request, ("Order deleted"))
    return redirect(request.META.get("HTTP_REFERER"))
  else:
    messages.success(request, ("Error deleting order"))
    return redirect(request.META.get("HTTP_REFERER"))