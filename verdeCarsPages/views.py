from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import random
from datetime import datetime
from .models import User, Car
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse

import json
from .forms import UserForm, LoginForm, UpdateStranded, ClockHours, RequestRetrieval
from django.contrib.sessions.backends.db import SessionStore




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
                        request.session['user_id'] = savedUser.usernm
                        request.session['user_type'] = savedUser.userType

                        if savedUserType == "Customer":
                            return render(request, 'verdeCarsPages/customerHome.html')
                        # else if savedUserType == "Customer Service":
                        #     return render(request, 'verdeCarsPages/')
                        elif savedUserType == "Retrieval Specialist":
                            return render(request, 'verdeCarsPages/retrievalHome.html')
                        elif savedUserType == "Admin":
                            return render(request, 'verdeCarsPages/adminHome.html')
                        else:
                            return render(request, 'verdeCarsPages/index.html', context=context)
        
        if 'create_user' in request.POST:

            new_user_form = UserForm(request.POST or None)
            if new_user_form.is_valid():
                new_user_form.save()


    return render(request, 'verdeCarsPages/login.html', context=context)


def reservecar(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Customer' or user_type == 'Admin') :
        return render(request, 'verdeCarsPages/error403.html')
    else:
        if request.method == "POST":
        
            make = request.POST.get("make")
            model = request.POST.get("model")
            year = request.POST.get("year")
            imageUrl = request.POST.get("imageUrl")
            cost = request.POST.get("cost")
            car = Car.objects.get(make=make, model=model, year=year, cost=cost)
            car.isRented = True
            car.save()
            # Do something with the car info here
            return render(request, "verdeCarsPages/reserve-car.html", {"car": {"make": make, "model": model, "year": year, "cost": cost, 'ImageUrl': imageUrl}})
        else:
            return render(request, "verdeCarsPages/reserve-car.html")


def checkoutConfirmation(request):
    user_id = request.session.get('user_id')
    current_user = user_id
    code = random.randint(1111,9999)
    markInsured = False
    user_type = request.session.get('user_type')
    if not (user_type == 'Customer' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        
        
        if request.method == "POST":
            code = random.randint(1111,9999)
            make = request.POST.get("make")
            model = request.POST.get("model")
            year = request.POST.get("year")
            cost = request.POST.get("cost")
            address = request.POST.get("content")
            money = request.POST.get("payment")
            money = int(money)
            date = request.POST.get("rentaldate")
            insured = request.POST.get("insurance")
            currentUser = User.objects.get(usernm=user_id)
            currentUser.money = float(currentUser.money) - float(cost)
            currentUser.save()

            
            if insured == "on":
                markInsured == True
                cost = float(cost)+50
            if date == "":
                context = {
                    "car": {"make": make, "model": model, "year": year, "cost": cost},
                    'error': "Please select a date"
                    }
                return render(request, 'verdeCarsPages/reserve-car.html', context)
            if address == "":
                context = {
                    "car": {"make": make, "model": model, "year": year, "cost": cost},
                    'error': "Please enter a billing address!"
                    }
                return render(request, 'verdeCarsPages/reserve-car.html', context)
            if money < float(cost):
                    context = {
                    "car": {"make": make, "model": model, "year": year, "cost": cost},
                    'error': "Please Enter enough to pay for your vehicle and any insurance you wish to purchase."
                    }
                    return render(request, 'verdeCarsPages/reserve-car.html', context) 
            return render(request, 'verdeCarsPages/checkout-confirmation.html', {"car": {"make": make, "model": model, "year": year, "cost": cost, 'code': code}})



def strandedCar(request, car_id):
    user_type = request.session.get('user_type')
    if not (user_type == 'Retrieval Specialist' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        car = get_object_or_404(Car, pk=car_id)
        userData = User.objects.filter(checkoutCode=str(car.checkoutCode)).values()
        updateStranded = UpdateStranded()
        context = {'car': car, 'userData': userData, 'updateStranded' : updateStranded}

        if request.method == "POST":
            if 'update_stranded' in request.POST:
                car.stranded = False
                car.strandedAddress = ""
                car.save()
        return render(request, 'verdeCarsPages/strandedCar.html', context)


def catalog(request):
    user_type = request.session.get('user_type')
    print(user_type)
    if not (user_type == 'Customer' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        cars = Car.objects.all()
        return render(request, 'verdeCarsPages/catalog.html', {'cars': cars}) 

def retrievalList(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Retrieval Specialist' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        strandedCars = Car.objects.filter(stranded=True)
        return render(request, 'verdeCarsPages/retrievalList.html', {'strandedCars': strandedCars})

def retrievalHome(request):
    user_type = request.session.get('user_type')

    if not (user_type == 'Retrieval Specialist' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        return render(request, 'verdeCarsPages/retrievalHome.html')
    

def clockHours(request):
    user_type = request.session.get('user_type')

    if not (user_type == 'Retrieval Specialist' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        user_id = request.session.get('user_id')
        currentUser = User.objects.get(usernm=user_id)
        clockHours = ClockHours
        context = {'clockHours': clockHours, 'user_id': user_id, 'user': currentUser}

        if request.method == "POST":
            hoursForm = ClockHours(request.POST or None)
            
            if hoursForm.is_valid():
                hoursLogged = hoursForm.cleaned_data.get('hoursWorked')
                currentUser.hoursWorked += hoursLogged
                currentUser.save()

        return render(request, 'verdeCarsPages/clockHours.html', context)



def adminHome(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else: 
        admin = User.objects.get(userType="Admin")
        context = {
            'earnings': admin.money,
            'cust_service_set': User.objects.filter(userType='Customer Service'),
            'retrieval_set': User.objects.filter(userType='Retrieval Specialist'),
        }
        if request.method == "POST":
            identity = request.POST['identity']
            u = User.objects.get(id=identity)
            earned = (u.hoursWorked*10)
            u.money=u.money+earned
            u.hoursWorked=0
            u.save()
            admin.money = admin.money - earned
            admin.save()
            context = {
            'earnings': admin.money,
            'cust_service_set': User.objects.filter(userType='Customer Service'),
            'retrieval_set': User.objects.filter(userType='Retrieval Specialist'),
            }
            # return render(request, 'verdeCarsPages/adminHome.html', context)
        return render(request, 'verdeCarsPages/adminHome.html', context)


def customerHome(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Customer' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        return render(request, 'verdeCarsPages/customerHome.html')


def requestRetrieval(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Customer'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        if request.method == "POST":
                requestRetrieval = RequestRetrieval(request.POST or None)
                if requestRetrieval.is_valid():
                    checkoutCode = requestRetrieval.cleaned_data.get('checkoutCode')
                    strandedAddress = requestRetrieval.cleaned_data.get('strandedAddress')

                    for car in Car.objects.all():
                        if checkoutCode == car.checkoutCode:
                            car.stranded = True
                            car.strandedAddress = strandedAddress
                            car.save()

                            if car.insured == False:
                                for savedUser in User.objects.all():
                                    if checkoutCode == savedUser.checkoutCode:
                                        savedUser.money -= 300
                                        savedUser.save()

        return render(request, 'verdeCarsPages/requestRetrieval.html')

def addMoney(request):
    user_type = request.session.get('user_type')
    user_id = request.session.get('user_id')
    if not (user_type == 'Customer' or user_type == 'Admin'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        user_id = request.session.get('user_id')
        current_user = User.objects.get(usernm=user_id)
        balance = int(current_user.money)
        print("money" + str(balance))

        context = {
            'currentMoney': balance
        }

        if request.method == "POST":
            money = request.POST.get("payment")
            if money.isdigit() == False:
                context = {
                'currentMoney': balance,
                'error': "Please Enter a valid number"
                }
                return render(request, 'verdeCarsPages/add-money.html', context)
            balance = balance + int(money)
            current_user.money = balance
            current_user.save()
            context = {
                    'currentMoney': balance}
        return render(request, 'verdeCarsPages/add-money.html', context)


def unrentCar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        make = data.get("make")
        model = data.get("model")
        year = data.get("year")
        
        # Get the car object from the database
        car = Car.objects.get(make=make, model=model, year=year)
        
        # Update the isRented field to False
        car.isRented = False
        car.save()
        return JsonResponse({'success': True})