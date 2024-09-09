# Generated by Django 5.1 on 2024-09-09 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0006_fleetform_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourform',
            name='country_code',
            field=models.CharField(default=(), max_length=5, verbose_name='Country Code'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fleetform',
            name='country_code',
            field=models.CharField(max_length=5, verbose_name='Country Code'),
        ),
    ]
