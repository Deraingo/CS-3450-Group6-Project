from unicodedata import name
from django.urls import path, include

from . import views

app_name = 'verdeCarsPages'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('reserve-car/', views.reservecar, name='reservecar'),
    path('checkout-confirmation/', views.checkoutConfirmation, name='checkoutConfirmation')
    path('retrievalPage/', views.retrievalPage, name='retrievalPage'),
    path('catalog/', views.catalog, name='catalog'),
]