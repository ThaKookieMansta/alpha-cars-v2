"""
This file consist of the filtering mechanism for the cars page.
"""
import django_filters
from .models import Car
from django import forms


class CarFilter(django_filters.FilterSet):
    """
    This class defines how the filter works in the cars page when
    a user wants to search for a car
    """
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