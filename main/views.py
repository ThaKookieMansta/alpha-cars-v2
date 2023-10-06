"""
This file contains the various views that are used in this project
"""
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car, Image
from django.conf import settings
from .filters import CarFilter


# Create your views here.

def index(request):
    """
    This view handles the data passed in the
    homepage of the web app
    Args:
        request:

    Returns:

    """
    cars = Car.objects.all().order_by('-id')
    today = datetime.date.today()
    year = today.year
    return render(request, 'main/index.html', {
        'cars': cars[:3],
        "year": year,
    })


def carView(request, id, carSlug):
    """
    This view handles the data passed in the page
    of a selected car in the web app
    Args:
        request:
        id: The id of the car from the Database
        carSlug: Thhis forms the link to the page.

    Returns:

    """
    today = datetime.date.today()
    year = today.year
    # image_urls = Image._meta.fields

    try:
        cars = Car.objects.get(id=id)
        # This section is where we get the urls for the images stored in the
        # Image model and pass them as a list to the template.
        image_urls = []
        for field in cars.images._meta.fields:  # This is accessing the images field in the Car model.
            if field.name.startswith('image_'):
                image_url = getattr(cars.images, field.name)
                if image_url:
                    image_urls.append(image_url)
        return render(request, 'main/car-details.html', {
            "details": True,
            "car": cars,
            "pics": image_urls,
            "year": year,
            "MEDIA_URL": settings.MEDIA_URL,
            # Do not forget to pass this as you will manually complete the URL in the template.
        })
    except Exception as exc:
        return render(request, 'main/car-details.html', {
            "details": False,
            "year": year,
        })

def all_cars(request):
    """
    This view displays all the cars that are in the database to the
    cars page.
    Args:
        request:

    Returns:

    """
    cars = Car.objects.all().order_by('-id')
    today = datetime.date.today()
    year = today.year
    car_filter = CarFilter(request.GET, queryset=cars)
    cars= car_filter.qs
    return render(request, 'main/cars.html', {
        "year": year,
        "cars": cars,
        "car_filter": car_filter,
    })

def about_us(request):
    """
    This view displays the about us details
    Args:
        request:

    Returns:

    """
    today = datetime.date.today()
    year = today.year
    return render(request, 'main/about-us.html', {
        "year": year,
    })

def terms(request):
    """
    This view parses the html page for terms and conditions
    Args:
        request:

    Returns:

    """
    today = datetime.date.today()
    year = today.year
    return render(request, 'main/terms.html', {
        "year": year,
    })

def faq(request):
    """
    This view parses the html page for frequently asked questions
    Args:
        request:

    Returns:

    """
    today = datetime.date.today()
    year = today.year
    return render(request, 'main/faq.html', {
        "year": year,
    })