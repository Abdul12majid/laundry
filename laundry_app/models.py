from django.db import models

# Create your models here.

class ClotheType(models.Model):
	name = models.CharField('Name', max_length=40, blank=False)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Type of cloth'


class Service(models.Model):
	service_name = models.CharField(max_length=40, blank=False)
	price = models.IntegerField(blank=False)

	def __str__(self):
		return self.service_name

	


class Order(models.Model):
	details = models.TextField('Details', blank=False)
	order_Id = models.CharField('ID', max_length=40, blank=False)
	
	total_price = models.IntegerField(blank=True, null=True)
	service = models.CharField(max_length=40, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	

class Pre_order(models.Model):
	name =models.ManyToManyField(ClotheType, blank=True)
	