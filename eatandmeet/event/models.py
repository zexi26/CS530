from django.db import models
from menu.models import Product
# Create your models here.

class Event(models.Model):
	event_id = models.CharField(max_length=250, blank=True)
	date_added = models.DateField(auto_now_add=True)
	class Meta:
		db_table = 'Event'
		ordering = ['date_added']

	def __str__(self):
		return self.event_id

class EventItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	active = models.BooleanField(default=True)
	class Meta:
		db_table = 'EventItem'

	def sub_total(self):
		return self.product.price * self.quantity

	def __str__(self):
		return self.product