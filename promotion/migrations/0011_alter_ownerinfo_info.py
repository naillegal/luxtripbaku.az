# Generated by Django 5.1 on 2024-11-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0010_ownerinfo_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerinfo',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
