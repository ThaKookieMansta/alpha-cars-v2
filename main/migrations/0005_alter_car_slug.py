# Generated by Django 4.2 on 2023-04-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_car_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
