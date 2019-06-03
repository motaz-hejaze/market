from django.contrib import admin

# Register your models here.
from .models import Category , Product , Image , Information

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Information)