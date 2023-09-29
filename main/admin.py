from django.contrib import admin
from django.utils.text import slugify

from .models import CarDrive, Car, CarBodyType, TransmissionType, FuelType, SeatNo, Feature, Door, Image


# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "slug", "id",)
    list_filter = ("id", "make", "model")
    readonly_fields = ('slug',)
    # prepopulated_fields = {'slug': ('id', 'make', 'model',)}


admin.site.register(Image)
admin.site.register(Car, CarAdmin)
admin.site.register(CarDrive)
admin.site.register(CarBodyType)
admin.site.register(TransmissionType)
admin.site.register(FuelType)
admin.site.register(SeatNo)
admin.site.register(Feature)
admin.site.register(Door)
