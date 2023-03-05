from unicodedata import name
from django.urls import path, include

from . import views

app_name = 'verdeCarsPages'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/<int:form_id>/edit', views.login, name='login'),
]