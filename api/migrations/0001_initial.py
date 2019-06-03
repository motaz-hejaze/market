# Generated by Django 2.2.1 on 2019-06-02 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='اسم الفئة')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=50)),
                ('phone1', models.CharField(max_length=20, null=True)),
                ('phone2', models.CharField(max_length=20, null=True)),
                ('work_start_hour', models.IntegerField()),
                ('work_start_period', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], default='am', max_length=20)),
                ('work_end_hour', models.IntegerField()),
                ('work_end_period', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], default='pm', max_length=20)),
                ('whatsapp', models.CharField(max_length=50, null=True)),
                ('facebook', models.CharField(max_length=50, null=True)),
                ('twitter', models.CharField(max_length=50, null=True)),
                ('pinterest', models.CharField(max_length=50, null=True)),
                ('google', models.CharField(max_length=50, null=True)),
                ('delivery_available', models.BooleanField(default=False)),
                ('payment', models.CharField(choices=[('cash', 'Cash'), ('visa', 'Visa'), ('both', 'Both')], default='cash', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('number_in_stocks', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('path', models.ImageField(upload_to='products_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='api.Product')),
            ],
        ),
    ]
