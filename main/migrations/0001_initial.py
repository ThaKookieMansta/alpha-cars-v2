# Generated by Django 4.2 on 2023-04-13 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBodyType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('bodyType', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CarDrive',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('driveType', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('doors', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('featureName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('fuelType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SeatNo',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('seats', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionType',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('transmission', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('images', models.ImageField(upload_to='images')),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('make', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('yom', models.CharField(max_length=250)),
                ('mileage', models.CharField(max_length=250)),
                ('eng_capacity', models.CharField(max_length=250)),
                ('chassis', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('ext_color', models.CharField(max_length=50)),
                ('int_color', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carbodytype')),
                ('doors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.door')),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cardrive')),
                ('features', models.ManyToManyField(to='main.feature')),
                ('fuel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fueltype')),
                ('seats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seatno')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transmissiontype')),
            ],
        ),
    ]