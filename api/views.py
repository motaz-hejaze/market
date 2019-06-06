from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Category , Information , Product
from .serializers import CategorySerializer ,ProductSerializer , InfoSerializer



class CategoryView(APIView):
	def get(self,request):
		categories = Category.objects.all()
		print(categories)
		serializer = CategorySerializer(categories , many=True)
		print(serializer)
		return Response({"categories":serializer.data})



	def post(self,request):
		category = request.data.get('category')
		serializer = CategorySerializer(data=category)
		if serializer.is_valid(raise_exception=True):
			category_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Category {} successfully created".format(category_saved.name)
			})


	def put(self,request,pk):
		saved_category = get_object_or_404(Category,pk=pk)
		data = request.data.get('category')
		serializer = CategorySerializer(instance=saved_category,data=data,partial=True)
		if serializer.is_valid(raise_exception=True):
			category_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Category {} successfully updated".format(category_saved.name)
			})


	def delete(self,request,pk):
		category = get_object_or_404(Category, pk=pk)
		category.delete()
		return Response({
			"status":"success",
			"message":"Category {} successfully deleted".format(category.name)
			})

	

class ShowCategory(APIView):
	def get(self,request,pk):
		category = get_object_or_404(Category,pk=pk)
		serializer = CategorySerializer(category)
		return Response({"category":serializer.data})

class CategoryCount(APIView):
	def get(self,request):
		categories_count = Category.objects.count()
		return Response({"Number of Categories": categories_count})

class CategoryProducts(APIView):
	def get(self,request,pk):
		category = get_object_or_404(Category,pk=pk)
		products = Product.objects.filter(category__id=pk).all()
		serializer = ProductSerializer(products , many=True)
		return Response({"category products":serializer.data})

class ProductView(APIView):
	def get(self,request):
		products = Product.objects.all()
		print(products)
		serializer = ProductSerializer(products , many=True)
		print(serializer)
		return Response({"products":serializer.data})



	def post(self,request):
		product = request.data.get('product')
		serializer = ProductSerializer(data=product)
		if serializer.is_valid(raise_exception=True):
			product_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Product {} successfully created".format(product_saved.name)
			})


	def put(self,request,pk):
		saved_product = get_object_or_404(Product,pk=pk)
		data = request.data.get('product')
		serializer = ProductSerializer(instance=saved_product,data=data,partial=True)
		if serializer.is_valid(raise_exception=True):
			product_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Product {} successfully updated".format(product_saved.name)
			})


	def delete(self,request,pk):
		product = get_object_or_404(Product, pk=pk)
		product.delete()
		return Response({
			"status":"success",
			"message":"Product {} successfully deleted".format(product.name)
			})


class ShowProduct(APIView):
	def get(self,request,pk):
		product = get_object_or_404(Product,pk=pk)
		product_serializer = ProductSerializer(product)
		product_images = Image.objects.filter(product__id=pk).all()
		image_serializer = ImageSerializer(product_images , many=True)
		return Response({
			"product data":product_serializer.data,
			"product images":image_serializer.data,
			})


class ProductCount(APIView):
	def get(self,request):
		products_count = Product.objects.count()
		return Response({"Number of Products": products_count})


class InfoView(APIView):
	def get(self,request):
		infos = Information.objects.all()
		serializer = InfoSerializer(infos , many=True)
		return Response({"informtions":serializer.data})



	def post(self,request):
		info = request.data.get('info')
		serializer = InfoSerializer(data=info)
		if serializer.is_valid(raise_exception=True):
			info_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Information {} successfully created".format(info_saved.name)
			})


	def put(self,request,pk):
		saved_info = get_object_or_404(info,pk=pk)
		data = request.data.get('info')
		serializer = InfoSerializer(instance=saved_info,data=data,partial=True)
		if serializer.is_valid(raise_exception=True):
			info_saved = serializer.save()
		return Response({
			"status":"success",
			"message":"Information {} successfully updated".format(info_saved.name)
			})


	def delete(self,request,pk):
		info = get_object_or_404(info, pk=pk)
		info.delete()
		return Response({
			"status":"success",
			"message":"Information {} successfully deleted".format(info.name)
			})

class ShowInfo(APIView):
	def get(self,request,pk):
		info = get_object_or_404(Information,pk=pk)
		serializer = InfoSerializer(info)
		return Response({"Information":serializer.data})