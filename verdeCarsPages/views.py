from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .models import User, Car
from .forms import UserForm, LoginForm


def index(request):
    return render(request, 'verdeCarsPages/index.html')


def login(request):
    allUsers = User.objects.all
    user_form = UserForm()
    login_form = LoginForm()

    context = {
        'user_form': user_form,
        'login_form': login_form,
        'all': allUsers,
    }

    if request.method == "POST":
        if 'login_user' in request.POST:
            
            new_login_form = LoginForm(request.POST or None)
            if new_login_form.is_valid():
                user_data = new_login_form.cleaned_data.get('usernm')
                pass_data = new_login_form.cleaned_data.get('passwd')
                for savedUser in User.objects.all():
                    if user_data == savedUser.usernm and pass_data == savedUser.passwd:
                        savedUserType = savedUser.userType
                        # FOR ALL: SEND THE USER TO THE HOMEPAGE OF THEIR RESPECTIVE USER TYPE
            return render(request, 'verdeCarsPages/index.html', context=context) # delete this and replace it with the homepage for their user type :)
            # else:
            #     return render(request, 'verdeCarsPages/login.html', context=context)
        
        if 'create_user' in request.POST:

            new_user_form = UserForm(request.POST or None)
            if new_user_form.is_valid():
                new_user_form.save()
            #     return render(request, 'verdeCarsPages/login.html', context=context)

            # else:
            #     return render(request, 'verdeCarsPages/login.html', context=context)


    return render(request, 'verdeCarsPages/login.html', context=context)


def reservecar(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
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

def retrievalHome(request):
    return render(request, 'verdeCarsPages/retrievalHome.html')

def adminHome(request):
    #user_set = User.objects.all
    context = {
        'customer_set': User.objects.filter(userType='Customer'),
        'admin_set': User.objects.filter(userType='Customer'),
        'cust_service_set': User.objects.filter(userType='Customer'),
        'retrieval_set': User.objects.filter(userType='Customer'),
    }
    return render(request, 'verdeCarsPages/adminHome.html', context)

