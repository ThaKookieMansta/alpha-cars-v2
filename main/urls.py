from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>/<slug:carSlug>/', views.carView, name='carDetails'),
    path('catalogue/', views.all_cars, name='allCars'),
    path('about-us/', views.about_us, name='aboutUs'),
    path('terms/', views.terms, name='terms'),
    path('frequently-asked-questions/', views.faq, name='faq'),

]