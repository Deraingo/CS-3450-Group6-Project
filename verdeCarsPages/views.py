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

from .forms import UserForm, LoginForm, UpdateStranded, ClockHours



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
    print(request)
    if request.method == "POST":
        
        make = request.POST.get("make")
        model = request.POST.get("model")
        year = request.POST.get("year")
        imageUrl = request.POST.get("imageUrl")
        cost = request.POST.get("cost")
        print(cost)
        print("image: " + str(imageUrl))
        car = Car.objects.get(make=make, model=model, year=year)
        #car.isRented = True
        car.save()
        # Do something with the car info here
        return render(request, "verdeCarsPages/reserve-car.html", {"car": {"make": make, "model": model, "year": year, "cost": cost, 'ImageUrl': imageUrl}})
    else:
        return render(request, "verdeCarsPages/reserve-car.html")



def checkoutConfirmation(request):
    current_user = request.user
    code = random.randint(1111,9999)
    markInsured = False
    
    if request.method == "POST":
        make = request.POST.get("make")
        model = request.POST.get("model")
        year = request.POST.get("year")
        car = Car.objects.get(make=make, model=model, year=year)
        money = int(request.POST.get("payment"))
        date = request.POST.get("rentaldate")
        insured = request.POST.get("insurance")
        if insured == "on":
            markInsured = True
            money = money+50
    
    if request.user.is_authenticated:
        current_user.money = current_user.money - money
        current_user.checkoutCode = code
        current_user.save()
        car.rentalStart = date
        car.rentalEnd = date
        car.checkoutCode = code
        car.insured = markInsured

        context= {
            'code': code,
            'test': money
        }    
        
        #car.checkoutCode = code
        return render(request, 'verdeCarsPages/checkout-confirmation.html', context)
    else:
        context= {
            'code': code,
            'test': make
        } 
        return render(request, 'verdeCarsPages/checkout-confirmation.html', context)
    return render(request, 'verdeCarsPages/checkout-confirmation.html')



def strandedCar(request, car_id):
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
    # if not (request.user.is_authenticated and request.user.userType == 'Customer'):
    #     return render(request, 'verdeCarsPages/error403.html')
        
    # else:
        cars = Car.objects.all()
        return render(request, 'verdeCarsPages/catalog.html', {'cars': cars}) 

def retrievalList(request):
    strandedCars = Car.objects.filter(stranded=True)
    return render(request, 'verdeCarsPages/retrievalList.html', {'strandedCars': strandedCars})

def retrievalHome(request):
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
    return render(request, 'verdeCarsPages/customerHome.html')


def requestRetrieval(request):
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
    inputMoney = InputMoney
    
    if request.user.is_authenticated:
        context = {'inputMoney': inputMoney,
              'currentMoney': current_user.money}
    else:
        return render (request, 'verdeCarsPages/error403.html')
    if request.method == "POST":
        moneyForm = InputMoney(request.POST or None)
        
        if moneyForm.is_valid():
            userName = hoursForm.cleaned_data.get('usernm')
            passWord = hoursForm.cleaned_data.get('passwd')
            moneyInputed = moneyForm.cleaned_data.get('money')
            for savedUser in User.objects.all():
                if savedUser.usernm == userName and savedUser.passwd == passWord:
                    savedUser.money = savedUser.money+moneyInputed
                    context = {'inputMoney': inputMoney,
                              'currentMoney': 0}
            


    return render(request, 'verdeCarsPages/add-money.html', context)
