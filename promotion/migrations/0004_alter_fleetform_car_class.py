# Generated by Django 5.1 on 2024-08-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0003_car_name_en_car_name_ru_city_name_en_city_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleetform',
            name='car_class',
            field=models.CharField(choices=[('any', 'Any'), ('economy', 'Economy'), ('comfort', 'Comfort'), ('business', 'Business'), ('premium', 'Premium'), ('vip', 'VIP'), ('suv', 'SUV'), ('van', 'Van'), ('minibus', 'Minibus'), ('bus', 'Bus')], max_length=255),
        ),
    ]