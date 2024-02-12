from django.shortcuts import render, redirect
from .models import ClotheType, Pre_order, Service, Order
from django.views.decorators.csrf import csrf_protect
import json
from django.http import JsonResponse


# Create your views here.
def home(request):
	if request.method == 'POST':
		name = request.POST['data']
		return redirect('/admin')
	return render(request, 'index.html', )


def settings(request):
	return render(request, 'settings.html', )

def dashboard(request):
	return render(request, 'dashboard.html', )


def index(request):
  services = Service.objects.all()
  clothes = ClotheType.objects.all()
  return render(request, 'index_.html', {'services':services, 'clothes':clothes})


def dynamic_data(request):
  if request.method == 'GET':
    service_id = request.GET.get('service_id')
    x = int(service_id)
    print(x)
    try:
      service = Service.objects.get(pk=x)
     # if service.id == 1:
      #  dynamic_field_value = 100
      #elif service.id == 2:
       # dynamic_field_value = 200
      #elif service.id == 3:
       # dynamic_field_value = 300
      #else:
      dynamic_field_value = 4  # Set a default value for other cases
      print(dynamic_field_value)

      # Determine how to dynamically generate the input field value/attributes
      # Replace with your logic (e.g., calculate value based on service data)
      
      # ... (Optionally, set other attributes for the input field)
      return JsonResponse({'value': dynamic_field_value})
    except service.DoesNotExist:
      return JsonResponse({'error': 'Invalid service ID'}, status=404)
  else:
    return HttpResponseBadRequest('Invalid request method')




def order(request):
	if request.method == 'POST':
		number = request.POST[0]
		#action = request.POST[]
		return render(request, 'receipt.html', {'number':number, 'action':action})
	return render(request, 'receipt.html', {})


@csrf_protect
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	if request.user.is_authenticated:
		total = float(data['form']['total'])
		x = Action.objects.create(action_name=total)
		x.save()
		messages.success('request', ('helooo'))
	else:
		print('User is not logged in')
	return JsonResponse('Payment complete', safe=False)


l = []

@csrf_protect
def save_data(request):
  
  if request.method == 'POST':
    data = json.loads(request.body)
    content = data['content']
    order_id = data['xxx']
    price = data['total_price']
    clothes = data['total_clothes']
    services = data['total_service']
    new_record = Order.objects.create(details=clothes, order_Id=order_id, total_price=price, service=services)
    new_record.save()
    print(new_record)
    return JsonResponse({'success': True})
  else:
    return JsonResponse({'error': 'Invalid request method'})



