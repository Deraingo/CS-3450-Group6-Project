from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .models import User, Car
from .forms import UserForm


def index(request):
    return render(request, 'verdeCarsPages/index.html')


def login(request):
    allUsers = User.objects.all
    if request.method == "POST":
        form = UserForm(request.POST or None)  # Pass in 'None' if the user entered nothing into the form
        if form.is_valid():
            form.save()
        return render(request, 'verdeCarsPages/login.html', {'all': allUsers})  # Pass allUsers into the page so that it can be used for authentication later
        
    else:
        return render(request, 'verdeCarsPages/login.html', {'all': allUsers})

def reservecar(request):
    return render(request, 'verdeCarsPages/reserve-car.html')

def checkoutConfirmation(request):
    return render(request, 'verdeCarsPages/checkout-confirmation.html')

def strandedCar(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, 'verdeCarsPages/strandedCar.html', context)

def catalog(request):
    return render(request, 'verdeCarsPages/catalog.html')

def retrievalList(request):
    strandedCars = Car.objects.filter(stranded=True)
    return render(request, 'verdeCarsPages/retrievalList.html', {'strandedCars': strandedCars})

def adminHome(request):
    return render(request, 'verdeCarsPages/adminHome.html')

