from unicodedata import name
from django.urls import path, include

from . import views

app_name = 'verdeCarsPages'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/<int:form_id>/edit', views.login, name='login'),
    path('reserve-car/', views.reservecar, name='reservecar'),
    path('checkout-confirmation/', views.checkoutConfirmation, name='checkoutConfirmation'),
    path('<int:car_id>/', views.strandedCar, name='strandedCar'),
    path('catalog/', views.catalog, name='catalog'),
    path('retrievalList/', views.retrievalList, name='retrievalList'),
    path('retrievalHome/', views.retrievalHome, name='retrievalHome'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('requestRetrieval/', views.requestRetrieval, name="requestRetrieval"),
]
