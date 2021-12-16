from django.db import models
from location_field.models.plain import PlainLocationField
from users.models import User
# Create your models here.


class Routes (models.Model):
    name = models.CharField(max_length=50)

class Stationes (models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=255)
    locationStation = PlainLocationField(based_fields=['city'], zoom=7)
class Buses (models.Model):
    city = models.CharField(max_length=255, default=None )
    locationBus = PlainLocationField(based_fields=['city'], zoom=7 ,default=None)
    Route = models.ForeignKey(Routes, on_delete=models.CASCADE)

class Driver (models.Model):
    name = models.CharField(max_length=50)
    Bus = models.ForeignKey(Buses, on_delete=models.CASCADE)
    Rate = models.IntegerField(default=0)

class RoutesStation (models.Model):
    Route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    Station = models.ForeignKey(Stationes, on_delete=models.CASCADE)

class UserTicket (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)




