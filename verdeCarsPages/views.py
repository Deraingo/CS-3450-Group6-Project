from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from datetime import datetime
from .forms import UserForm


def index(request):
    return render(request, 'verdeCarsPages/index.html')

def login(request):
    if request.method == "POST":
        # If the user posts something, either take what they filled out
        # and turn it into a Form object, or if the form was empty, pass in None
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save
        return render(request, 'verdeCarsPages/join.html', {})
        
    else:
        return render(request, 'verdeCarsPages/login.html', {})
