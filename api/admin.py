from django.contrib import admin
from imagekit.admin import AdminThumbnail
# Register your models here.
from .models import Category , Product , Information

admin.site.register(Category)
admin.site.register(Information)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'number_in_stocks',  'image_display_main']
    image_display_main = AdminThumbnail(image_field='main_image')
    image_display_main.short_description = 'main_image'
    image_display_second = AdminThumbnail(image_field='second_image')
    image_display_second.short_description = 'second_image'
    image_display_third = AdminThumbnail(image_field='third_image')
    image_display_third.short_description = 'third_image'
    readonly_fields = ['image_display_main' , 'image_display_second', 'image_display_third']  # this is for the change form