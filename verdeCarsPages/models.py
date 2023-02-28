from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    usernm = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    userType = models.CharField(max_length=50)
    money = models.DecimalField(decimal_places=2, max_digits=50)

class Car(models.Model):
    cost = models.DecimalField(decimal_places=2, max_digits=50)
    availability = models.BooleanField()
    rentalStart = models.DateTimeField()
    rentalEnd = models.DateTimeField()
    checkoutCode = models.IntegerField()
    stranded = models.BooleanField()
