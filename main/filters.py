import django_filters
from .models import Car
from django import forms


class CarFilter(django_filters.FilterSet):
    make = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Car Make'
    )
    model = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Car Model'
    )

    class Meta:
        model = Car
        fields = ['body_type', 'make', 'model', 'fuel', 'transmission']