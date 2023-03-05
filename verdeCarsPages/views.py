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
        'create_user_form': user_form,
        'login_form': login_form,
        'all': allUsers,
    }

    if request.method == "POST":
        if 'create_user' in request.POST:
            user_form = UserForm()
            if user_form.is_valid():
                user_form.save()
                return render(request, 'verdeCarsPages/login.html', context=context)
        
        if 'enter_username' in request.POST and 'enter_password' in request.POST:
            login_form = LoginForm()
            if login_form.is_valid():
                user_data = login_form.cleaned_data.get("enter_username")
                pass_data = login_form.cleaned_data.get("enter_password")
                # if login_form.enter_username == 'Mary':

                context = {
                    'create_user_form': user_form,
                    'login_form': login_form,
                    'all': allUsers,
                    'user_data': user_data,
                    'pass_data': pass_data,
                }

                return render(request, 'verdeCarsPages/index.html/', context=context)

    return render(request, 'verdeCarsPages/login.html', context=context)
    