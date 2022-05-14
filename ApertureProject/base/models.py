from pyexpat import model
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

    def __str__(self):
        return self.Airplane_name

class Flight(models.Model):
    Date = models.DateField()
    flight_time = models.TimeField(default='00:00')
    Source_City = CountryField()
    Destination_City = CountryField()
    Flight_type = models.CharField(max_length=30)
    Flight_Duration = models.CharField(max_length=30)
    Boarding_Time = models.CharField(max_length=30)

    def __str__(self):
        return str(self.pk)

class Ticket(models.Model):
    SEAT_L = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    SEAT_N= (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    CABIN =(
        ('First', 'First'),
        ('Economy', 'Economy'),
        
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    Seat_location = models.CharField(max_length=1, choices=SEAT_L)
    Ticket_class = models.CharField(max_length=100, choices=CABIN, default='First')
    Seat_Number = models.CharField(max_length=2, choices=SEAT_N)
    Date_of_Issue = models.DateField(default=datetime.today)
    Flight_Number = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Booked(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Ticket_number = models.ForeignKey(Ticket , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Ticket_number)

class Waitlist(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Flight_Number = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.User)

class Bags(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Weight = models.CharField(max_length=20,default="23 KG")
    Dimensions = models.CharField(max_length=20)

    def __str__(self):
        return str(self.User)


