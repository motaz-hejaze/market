from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import Category , Image , Information , Product
from .serializers import CategorySerializer



class CategoryView(APIView):
	def get(self,request):
		categories = Category.objects.all()
		print(categories)
		serializer = CategorySerializer(categories , many=True)
		print(serializer)
		return Response({"categories":categories})

