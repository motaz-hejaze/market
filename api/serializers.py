from rest_framework import serializers
from .models import Category , Product , Information


class CategorySerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	name = serializers.CharField(max_length=60)
	description = serializers.CharField()


	def create(self,validated_data):
		return Category.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name' , instance.name)
		instance.description = validated_data.get('description' , instance.description)


		instance.save()

		return instance

class ProductSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	name = serializers.CharField(max_length=120)
	description = serializers.CharField(required=False)
	category_id = serializers.IntegerField()
	price = serializers.DecimalField(default=0.00 , decimal_places=2 , max_digits=8)
	number_in_stocks = serializers.IntegerField(default=0)
	main_image = serializers.ImageField()
	second_image = serializers.ImageField()
	third_image = serializers.ImageField()

	def create(self,validated_data):
		return Product.objects.create(**validated_data)


	def update(self,instance,validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.category_id = validated_data.get('category_id', instance.category_id)
		instance.price = validated_data.get('price', instance.price)
		instance.number_in_stocks = validated_data.get('number_in_stocks', instance.number_in_stocks)
		instance.main_image = validated_data.get('path' , instance.path)
		instance.second_image = validated_data.get('path' , instance.path)
		instance.third_image = validated_data.get('path' , instance.path)

		instance.save()

		return instance

"""
class ImageSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	name = serializers.CharField(max_length=60)
	product_id= serializers.IntegerField()
	description = serializers.CharField()
	path = serializers.ImageField()

	def create(self,validated_data):
		return Image.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name' , instance.name)
		instance.product_id = validated_data.get('product_id' , instance.product_id)
		instance.description = validated_data.get('description' , instance.description)
		instance.path = validated_data.get('path' , instance.path)


		instance.save()

		return instance
"""

class InfoSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	name = serializers.CharField(max_length=150)
	address = serializers.CharField(max_length=50)
	phone1 = serializers.CharField(max_length=20 , required=False)
	phone2 = serializers.CharField(max_length=20 , required=False)
	work_start_hour = serializers.IntegerField()
	work_start_period = serializers.CharField(max_length=20,default='am')
	work_end_hour = serializers.IntegerField()
	work_end_period = serializers.CharField(max_length=20,default='pm')
	whatsapp = serializers.CharField(max_length=50 , required=False)
	facebook = serializers.CharField(max_length=50 ,required=False)
	twitter = serializers.CharField(max_length=50 , required=False)
	pinterest = serializers.CharField(max_length=50 , required=False)
	google = serializers.CharField(max_length=50 , required=False)
	delivery_available = serializers.BooleanField(default=False)
	payment = serializers.CharField(max_length=20,default='cash')

	def create(self,validated_data):
		return Information.objects.create(**validated_data)

	def update(self,instance,validated_data):
		instance.name = validated_data.get('name' , instance.name)
		instance.address = validated_data.get('address' , instance.address)
		instance.phone1 = validated_data.get('phone1' , instance.phone1)
		instance.phone2 = validated_data.get('phone2' , instance.phone2)
		instance.work_start_hour = validated_data.get('work_start_hour' , instance.work_start_hour)
		instance.work_start_period = validated_data.get('work_start_period' , instance.work_start_period)
		instance.work_end_hour = validated_data.get('work_end_hour' , instance.work_end_hour)
		instance.work_end_period = validated_data.get('work_end_period' , instance.work_end_period)
		instance.whatsapp = validated_data.get('whatsapp' , instance.whatsapp)
		instance.facebook = validated_data.get('facebook' , instance.facebook)
		instance.twitter = validated_data.get('twitter' , instance.twitter)
		instance.pinterest = validated_data.get('pinterest' , instance.pinterest)
		instance.google = validated_data.get('google' , instance.google)
		instance.delivery_available = validated_data.get('delivery_available' , instance.delivery_available)
		instance.payment = validated_data.get('payment' , instance.payment)


		instance.save()

		return instance