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
        # if 'login_user' in request.POST:
        #     return render(request, 'verdeCarsPages/index.html', context=context)
            
        # login_form = LoginForm()
        # if login_form.is_valid():
        #     user_data = login_form.cleaned_data.get("enter_username")
        #     pass_data = login_form.cleaned_data.get("enter_password")
        #     if user_data in allUsers:
        #         return render(request, 'verdeCarsPages/index.html', context=context)
        
        if 'create_user' in request.POST:
            # return render(request, 'verdeCarsPages/index.html', context=context)

            new_user_form = UserForm()
            if new_user_form.is_valid():
                new_user_form.save()
                return render(request, 'verdeCarsPages/login.html', context=context)

            else:
                return render(request, 'verdeCarsPages/index.html', context=context)

    return render(request, 'verdeCarsPages/login.html', context=context)
    