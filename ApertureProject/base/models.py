from django.db import models
from datetime import datetime
# Create your models here.
from django_countries.fields import CountryField
from django.contrib.auth.models import User



class Person(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    DoB = models.DateField()
    Phone_num = models.CharField(max_length= 20)
    Address = models.CharField(max_length= 20)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER)

class Airplane(models.Model):
    Airplane_name = models.CharField(max_length=30, default='Airplane')
    Airplane_type = models.CharField(max_length=30)
    FirstFlightDate = models.DateField()
    LastFlightDate = models.DateField()
    FirstMaintenanceDate = models.DateField()
    LastMaintenanceDate = models.DateField()
    ON_MAINTENANCE = (
        ('T', 'Yes'),
        ('F', 'No'),
    )
    on_maintenance = models.CharField(max_length=1, choices = ON_MAINTENANCE, default='F')

class Flight(models.Model):
    Date = models.DateTimeField()
    Source_City = CountryField()
    Destination_City = CountryField()
    Flight_type = models.CharField(max_length=30)
    Flight_Duration = models.DurationField()
    Boarding_Time = models.CharField(max_length=30)

class Ticket(models.Model):
    Seat_location = models.CharField(max_length=100)
    Cabin = models.CharField(max_length=100)
    Seat_Number = models.CharField(max_length=100)
    Date_of_Issue = models.DateField(default=datetime.today)
    Flight_Number = models.ForeignKey(Flight, on_delete=models.CASCADE)

class Booked(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Ticket_number = models.ForeignKey(Ticket , on_delete=models.CASCADE)

class Waitlist(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Flight_Number = models.ForeignKey(Flight, on_delete=models.CASCADE)

class Bags(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Weight = models.CharField(default="23 KG")
    Dimensions = models.CharField()

