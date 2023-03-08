from datetime import date
from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12, default="000-000-0000")
    usernm = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    userType = models.CharField(max_length=50, default="Customer")
    money = models.FloatField(default=0.0)
    phoneNumber = models.CharField(max_length=10, default="000-000-0000")

    def __str__(self):
        return self.fname + " " + self.lname + " (" + self.userType + ")"




class Car(models.Model):
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=4, default="0000")
    cost = models.FloatField()
    rentalStart = models.DateTimeField()
    rentalEnd = models.DateTimeField()
    checkoutCode = models.IntegerField()
    stranded = models.BooleanField()
    stranded = models.BooleanField(default=False)
    imageURL = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.year)
