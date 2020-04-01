from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Product
from .models import Event, EventItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _event_id(request):
	event = request.session.session_key
	if not event:
		event = request.session.create()
	return event

def add_event(request, product_id):
	product = Product.objects.get(id=product_id)
	try:
		event = Event.objects.get(event_id=_event_id(request))
	except Event.DoesNotExist:
		event = Event.objects.create(
				event_id = _event_id(request)
		)
		event.save()
	try:
		event_item = EventItem.objects.get(product=product, event=event)
		if event_item.quantity <= event_item.product.stock:
			event_item.quantity += 1
		event_item.save()
	except EventItem.DoesNotExist:
		event_item = EventItem.objects.create(
					product = product,
					quantity = 1,
					event = event
			)
		event_item.save()
	return redirect('event:event_detail')

def event_detail(request, total=0, counter=0, event_item = None):
	try:
		event = Event.objects.get(event_id=_event_id(request))
		event_items = EventItem.objects.filter(event=event, active=True)
		for event_item in event_items:
			total += (event_item.product.price * event_item.quantity)
			counter += event_item.quantity
	except ObjectDoesNotExist:
		pass
	return render(request, 'event.html', dict(event_items = event_items, total = total, counter = counter))

def event_remove(request, product_id):
	event = Event.objects.get(event_id=_event_id(request))
	product = get_object_or_404(Product, id=product_id)
	event_item = EventItem.objects.get(product=product, event=event)
	if event_item.quantity > 1:
		event_item.quantity -= 1
		event_item.save()
	else:
		event_item.delete()
	return redirect('event:event_detail')

def full_remove(request, product_id):
	event = Event.objects.get(event_id=_event_id(request))
	product = get_object_or_404(Product, id=product_id)
	event_item = EventItem.objects.get(product=product, event=event)

	event_item.delete()
	return redirect('event:event_detail')