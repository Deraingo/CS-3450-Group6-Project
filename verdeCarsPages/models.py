from datetime import date
from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12, default="000-000-0000")
    usernm = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    userType = models.CharField(max_length=50, default="Customer") # Official user types are "Customer", "Customer Service", "Retrieval Specialist", or "Admin"
    money = models.FloatField(default=0.0)
    hoursWorked = models.IntegerField(default=0)
    checkoutCode = models.IntegerField(default=0000)

    def __str__(self):
        return self.fname + " " + self.lname + " (" + self.userType + ")"




class Car(models.Model):
    make = models.CharField(max_length=50, default="")
    model = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=4, default="0000")
    cost = models.FloatField()
    rentalStart = models.DateTimeField(default=None, null=True, blank=True)
    rentalEnd = models.DateTimeField(default=None, null=True, blank=True)
    checkoutCode = models.IntegerField(default=None, null=True, blank=True)
    stranded = models.BooleanField(default=False)
    strandedAddress = models.CharField(max_length=50, default="", blank=True, null=True)
    imageURL = models.CharField(max_length=1000, default="")
    isRented = models.BooleanField(default=False)
    insured = models.BooleanField(default=False)

    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.year)
