# Generated by Django 4.2 on 2023-04-15 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='month',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='yom',
            field=models.CharField(max_length=20),
        ),
    ]
