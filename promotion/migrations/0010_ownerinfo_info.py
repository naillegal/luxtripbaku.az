# Generated by Django 5.1 on 2024-11-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0009_ownerinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerinfo',
            name='info',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
    ]