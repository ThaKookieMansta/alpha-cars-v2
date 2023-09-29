from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class CarBodyType(models.Model):
    bodyType = models.CharField(max_length=30)

    def __str__(self):
        return self.bodyType


class TransmissionType(models.Model):
    transmission = models.CharField(max_length=20)

    def __str__(self):
        return self.transmission


class FuelType(models.Model):
    fuelType = models.CharField(max_length=20)

    def __str__(self):
        return self.fuelType


class CarDrive(models.Model):
    driveType = models.CharField(max_length=250)

    def __str__(self):
        return self.driveType


class SeatNo(models.Model):
    seats = models.CharField(max_length=10)

    def __str__(self):
        return self.seats


class Door(models.Model):
    doors = models.CharField(max_length=10)

    def __str__(self):
        return self.doors


class Feature(models.Model):
    featureName = models.CharField(max_length=250)

    def __str__(self):
        return self.featureName


class Image(models.Model):
    image_1 = models.ImageField(upload_to='images', blank=True)
    image_2 = models.ImageField(upload_to='images', blank=True)
    image_3 = models.ImageField(upload_to='images', blank=True)
    image_4 = models.ImageField(upload_to='images', blank=True)
    image_5 = models.ImageField(upload_to='images', blank=True)
    image_6 = models.ImageField(upload_to='images', blank=True)
    image_7 = models.ImageField(upload_to='images', blank=True)
    image_8 = models.ImageField(upload_to='images', blank=True)
    image_9 = models.ImageField(upload_to='images', blank=True)
    image_10 = models.ImageField(upload_to='images', blank=True)
    image_11 = models.ImageField(upload_to='images', blank=True)
    image_12 = models.ImageField(upload_to='images', blank=True)
    image_13 = models.ImageField(upload_to='images', blank=True)
    image_14 = models.ImageField(upload_to='images', blank=True)
    image_15 = models.ImageField(upload_to='images', blank=True)
    image_16 = models.ImageField(upload_to='images', blank=True)
    image_17 = models.ImageField(upload_to='images', blank=True)
    image_18 = models.ImageField(upload_to='images', blank=True)
    image_19 = models.ImageField(upload_to='images', blank=True)
    image_20 = models.ImageField(upload_to='images', blank=True)


class Car(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    images = models.OneToOneField(Image, on_delete=models.CASCADE)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    body_type = models.ForeignKey(CarBodyType, on_delete=models.CASCADE)
    transmission = models.ForeignKey(TransmissionType, on_delete=models.CASCADE)
    fuel = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    drive = models.ForeignKey(CarDrive, on_delete=models.CASCADE)
    seats = models.ForeignKey(SeatNo, on_delete=models.CASCADE)
    doors = models.ForeignKey(Door, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)
    yom = models.CharField(max_length=20)
    month = models.CharField(max_length=10)
    mileage = models.CharField(max_length=250)
    eng_capacity = models.CharField(max_length=250)
    chassis = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    ext_color = models.CharField(max_length=50)
    int_color = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now=True)
    is_reserved = models.BooleanField(default=False, verbose_name="Reserved")
    is_sold = models.BooleanField(default=False, verbose_name="Sold")
    price = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse("carView", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.make) + "-" + slugify(self.model)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make}({self.model}{self.slug}"
