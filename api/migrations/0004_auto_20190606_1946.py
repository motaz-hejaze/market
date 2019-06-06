# Generated by Django 2.2.1 on 2019-06-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190602_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='second_image',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='third_image',
            field=models.ImageField(null=True, upload_to='products_images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
