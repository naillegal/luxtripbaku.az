# Generated by Django 5.1 on 2024-11-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0008_fleetform_guest_number_tourform_guest_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sahibkarın Adı')),
                ('mobile', models.CharField(max_length=15, verbose_name='Mobil Nömrə')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Ünvanı')),
                ('image', models.ImageField(upload_to='owners/', verbose_name='Sahibkar Şəkili')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Görünür')),
            ],
        ),
    ]
