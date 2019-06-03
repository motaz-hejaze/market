from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=60 , verbose_name='اسم الفئة')
	description = models.TextField(blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



class Product(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(blank=True,null=True)
	category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='category_products' ,null=True)
	price = models.DecimalField(default=0.00 , decimal_places=2 , max_digits=8)
	number_in_stocks = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



class Image(models.Model):
	name = models.CharField(max_length=60)
	product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_images' , null=True)
	description = models.TextField(blank=True,null=True)
	path = models.ImageField(upload_to='products_images')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Information(models.Model):
	PAYMENT_METHODS = (
		('cash' , 'Cash'),
		('visa' , 'Visa'),
		('both' , 'Both'),
		)
	DAY_PERIODS = (
		('am' , 'AM'),
		('pm' , 'PM'),
		)
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=50)
	phone1 = models.CharField(max_length=20 , null=True)
	phone2 = models.CharField(max_length=20 , null=True)
	work_start_hour = models.IntegerField()
	work_start_period = models.CharField(max_length=20,choices=DAY_PERIODS,default='am')
	work_end_hour = models.IntegerField()
	work_end_period = models.CharField(max_length=20,choices=DAY_PERIODS,default='pm')
	whatsapp = models.CharField(max_length=50 , null=True)
	facebook = models.CharField(max_length=50 ,null=True)
	twitter = models.CharField(max_length=50 , null=True)
	pinterest = models.CharField(max_length=50 , null=True)
	google = models.CharField(max_length=50 , null=True)
	delivery_available = models.BooleanField(default=False)
	payment = models.CharField(max_length=20,choices=PAYMENT_METHODS,default='cash')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name