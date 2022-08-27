# Generated by Django 4.1 on 2022-08-27 17:41

import cloudinary.models
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.FloatField(max_length=100000)),
                ('image_url', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=1000)),
                ('rating', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Product Review',
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='catalog.orderitem')),
            ],
        ),
    ]
