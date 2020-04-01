from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from datetime import date
# from django.contrib.gis.db.models import PointField


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('menu:products_by_category', args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	# point = PointField(default='POINT(0.0 0.0)')
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE) #if a product is deleted, any references at the category model of that product will be deleted
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='product', blank=True)
	guest = models.DecimalField(max_digits=5, decimal_places=0)
	available = models.BooleanField(default=True)
	date = models.DateField(default=date.today)
	created = models.DateTimeField(auto_now_add=True) #add by default when a product is created
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('menu:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)