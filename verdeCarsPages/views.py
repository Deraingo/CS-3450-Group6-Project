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

def login(request, form_id):
    allUsers = User.objects.all

    user_form = UserForm()
    login_form = LoginForm()
    if request.method == "POST":
        if 'create_user' in request.POST:
            user_form = UserForm()
            if user_form.is_valid():
                user_form.save()
                return render(request, 'verdeCarsPages/login.html', {'all': allUsers})
        # if 'enter_login' in request.POST:
        #     login_form = LoginForm()
        #     if login_form.is_valid():
        #         login_form.save()
        #         return render(request, 'verdeCarsPages/login.html', {'all': allUsers})

    context = {
        'create_user_form': user_form,
        'login_form': login_form,
    }
        # form = LoginForm(request.POST or None)
        # if form.is_valid():
        #     form.save()
        # form = UserForm(request.POST or None)  # Pass in 'None' if the user entered nothing into the form
        # if form.is_valid():
        #     form.save()
    #     return render(request, 'verdeCarsPages/login.html', {'all': allUsers})  # Pass allUsers into the page so that it can be used for authentication later

    # else:
    
    return render(request, 'verdeCarsPages/login.html', context=context)
