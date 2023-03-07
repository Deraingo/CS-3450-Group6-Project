from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12, default="000-000-0000")
    usernm = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    userType = models.CharField(max_length=50, default="Customer")
    money = models.FloatField(default=0.0)



class Car(models.Model):
    cost = models.FloatField()
    availability = models.BooleanField()
    rentalStart = models.DateTimeField()
    rentalEnd = models.DateTimeField()
    checkoutCode = models.IntegerField()
    stranded = models.BooleanField()

    
