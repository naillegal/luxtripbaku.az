# Generated by Django 5.1 on 2024-08-19 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='cars/')),
                ('ban_type', models.CharField(max_length=50)),
                ('lux_type', models.CharField(max_length=50)),
                ('person_count', models.IntegerField(default=0)),
                ('luggage_count', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Add Car',
                'verbose_name_plural': 'Add Cars',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='City name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'City',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('website', models.URLField(blank=True, null=True)),
                ('additional_request', models.TextField(blank=True, null=True)),
                ('viewed', models.BooleanField(default=False, verbose_name='Baxdım')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Faq',
                'verbose_name_plural': 'Faqs',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='FleetForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_location', models.CharField(choices=[('gyd-airport', 'from GYD airport'), ('hotel', 'from Hotel')], max_length=255)),
                ('dropoff_location', models.CharField(max_length=255)),
                ('date_of_service', models.DateField()),
                ('time_of_service', models.TimeField()),
                ('car_class', models.CharField(choices=[('economy', 'Economy'), ('comfort', 'Comfort'), ('business', 'Business'), ('premium', 'Premium'), ('vip', 'VIP'), ('suv', 'SUV'), ('van', 'Van'), ('minibus', 'Minibus'), ('bus', 'Bus')], max_length=255)),
                ('flight_number', models.CharField(blank=True, max_length=50)),
                ('additional_request', models.TextField(blank=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('viewed', models.BooleanField(default=False, verbose_name='Baxdım')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')),
            ],
            options={
                'verbose_name': 'Fleet Form',
                'verbose_name_plural': 'Fleet Forms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='HomeFirstContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'Home First Content',
                'verbose_name_plural': 'Home First Contents',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OurInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('location', 'Location'), ('email', 'Email'), ('number', 'Number')], max_length=255, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('tiktok', 'TikTok'), ('whatsapp', 'WhatsApp'), ('wechat', 'WeChat')], max_length=20, unique=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UpdatesRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'UpdateRequest',
                'verbose_name_plural': 'UpdatesRequest',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PriceByWayCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way_count', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='promotion.car')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tour name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='promotion.city')),
            ],
            options={
                'verbose_name': 'Add Tours',
                'verbose_name_plural': 'Add Tours',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TourForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_tour_days', models.IntegerField(default=1)),
                ('travel_date', models.DateField()),
                ('car_class', models.CharField(choices=[('economy', 'Economy'), ('comfort', 'Comfort'), ('business', 'Business'), ('premium', 'Premium'), ('vip', 'VIP'), ('suv', 'SUV'), ('van', 'Van'), ('minibus', 'Minibus'), ('bus', 'Bus')], max_length=255)),
                ('additional_request', models.TextField(blank=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('viewed', models.BooleanField(default=False, verbose_name='Baxdım')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')),
                ('select_city', models.ManyToManyField(related_name='select_city', to='promotion.city')),
            ],
            options={
                'verbose_name': 'Tour Form',
                'verbose_name_plural': 'Tour Forms',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tours/', verbose_name='Tour image')),
                ('caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image caption')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='promotion.tour')),
            ],
            options={
                'verbose_name': 'Tour images',
                'verbose_name_plural': 'Tour images',
                'ordering': ['-created'],
            },
        ),
    ]
