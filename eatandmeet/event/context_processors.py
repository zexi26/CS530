from .models import Event, EventItem
from .views import _event_id

def counter(request):
	item_count = 0
	if 'admin' in request.path:
		return {}
	else:
		try:
			event = Event.objects.filter(event_id=_event_id(request))
			event_items = EventItem.objects.all().filter(event=event[:1])

			for event_item in event_items:
				item_count += event_item.quantity
		except Cart.DoesNotExist:
			item_count = 0
	return dict(item_count = item_count)