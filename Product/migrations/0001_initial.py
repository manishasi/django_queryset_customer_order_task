# Generated by Django 4.1.6 on 2023-03-31 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('total_Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_name', to='Product.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Product.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro', to='Product.products')),
            ],
        ),
    ]