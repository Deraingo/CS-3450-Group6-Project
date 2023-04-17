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
    if not (user_type == 'Customer') :
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
    current_user = request.user
    
    if request.method == "POST":
        code = random.randint(1111,9999)
        context= {
            'code': code
        }    
        current_user.checkoutCode = code
        #car.checkoutCode = code
        return render(request, 'verdeCarsPages/checkout-confirmation.html', context)
    return render(request, 'verdeCarsPages/checkout-confirmation.html')


def strandedCar(request, car_id):
    user_type = request.session.get('user_type')
    if not (user_type == 'Retrieval Specialist'):
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
    if not (user_type == 'Customer'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        cars = Car.objects.all()
        return render(request, 'verdeCarsPages/catalog.html', {'cars': cars}) 

def retrievalList(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Retrieval Specialist'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        strandedCars = Car.objects.filter(stranded=True)
        return render(request, 'verdeCarsPages/retrievalList.html', {'strandedCars': strandedCars})

def retrievalHome(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Retrieval Specialist'):
        return render(request, 'verdeCarsPages/error403.html')
    else:
        clockHours = ClockHours
        context = {'clockHours': clockHours}


        if request.method == "POST":
            hoursForm = ClockHours(request.POST or None)
            
            if hoursForm.is_valid():
                userName = hoursForm.cleaned_data.get('usernm')
                passWord = hoursForm.cleaned_data.get('passwd')
                hoursLogged = hoursForm.cleaned_data.get('hours')
                for savedUser in User.objects.all():
                    if savedUser.usernm == userName and savedUser.passwd == passWord:
                        savedUser.hoursWorked += hoursLogged
                        savedUser.save()
                        # return render(request, 'verdeCarsPages/retrievalHome.html', context)

        return render(request, 'verdeCarsPages/retrievalHome.html', context)

def adminHome(request):
    context = {
        'customer_set': User.objects.filter(userType='Customer'),
        'admin_set': User.objects.filter(userType='Customer'),
        'cust_service_set': User.objects.filter(userType='Customer Service'),
        'retrieval_set': User.objects.filter(userType='Customer'),
    }
    if request.method == "POST":
        identity = request.POST['identity']
        u = User.objects.get(id=identity)
        u.money=u.money+(u.hoursWorked*10)
        u.hoursWorked=0
        u.save()
    return render(request, 'verdeCarsPages/adminHome.html', context)


def customerHome(request):
    user_type = request.session.get('user_type')
    if not (user_type == 'Customer'):
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

                    for savedUser in User.objects.all():
                        if checkoutCode == savedUser.checkoutCode:
                            savedUser.money -= 300
                            savedUser.save()

        return render(request, 'verdeCarsPages/requestRetrieval.html')

def addMoney(request):
    current_user = request.user
    # inputMoney = InputMoney()
    
    # if request.user.is_authenticated:
    #     context = {'inputMoney': inputMoney,
    #           'currentMoney': current_user.money}
    # else:
    #     context = {'inputMoney': inputMoney,
    #           'currentMoney': 0}
    # if request.method == "POST":
    #     moneyForm = InputMoney(request.POST or None)
        
    #     if moneyForm.is_valid():
    #         userName = hoursForm.cleaned_data.get('usernm')
    #         passWord = hoursForm.cleaned_data.get('passwd')
    #         moneyInputed = moneyForm.cleaned_data.get('money')
    #         for savedUser in User.objects.all():
    #             if savedUser.usernm == userName and savedUser.passwd == passWord:
    #                 savedUser.money = savedUser.money+moneyInputed
    #                 context = {'inputMoney': inputMoney,
    #                           'currentMoney': 0}
            

    return render(request, 'verdeCarsPages/add-money.html')
    # return render(request, 'verdeCarsPages/add-money.html', context)


def unrentCar(request):
    print(request)
    print("yaya i fuck bees")
    
    if request.method == 'POST':
        data = json.loads(request.body)
        make = data.get("make")
        model = data.get("model")
        year = data.get("year")
        # print(request.content)
        print(make)
        print(model)
        print(year)
        
        # Get the car object from the database
        car = Car.objects.get(make=make, model=model, year=year)
        
        # Update the isRented field to False
        car.isRented = False
        car.save()
        return JsonResponse({'success': True})