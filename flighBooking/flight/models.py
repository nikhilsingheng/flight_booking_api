from django.db import models

# Create your models here.


class Flight(models.Model):
    fightNumber = models.CharField(max_length=10)
    operatingAirlines = models.CharField(max_length=20)
    departurCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

# -----------------if table is null or empty use blank=True and null=True -----------------#


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    emial = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)

    