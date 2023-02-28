from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'verdeCarsPages/index.html')

def reservecar(request):
    return render(request, 'verdeCarsPages/reserve-car.html')

def checkoutConfirmation(request):
    return render(request, 'verdeCarsPages/checkout-confirmation.html')

def retrievalPage(request):
    return render(request, 'verdeCarsPages/retrievalPage.html')

def catalog(request):
    return render(request, 'verdeCarsPages/catalog.html')

