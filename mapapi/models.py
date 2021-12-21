from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models import CharField


class driver(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)

    phone_validation = RegexValidator(regex=r'^01[5|1|2|0][0-9]{8}$',
                                      message=" Please ,, Entered the Phone number in the format: '010|212|134|156'.")
    mobile_phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=("Phone"))
    username = models.CharField(max_length=100)
    password: CharField = models.CharField(max_length=100)
    bus_number=models.IntegerField(null=True)
    def __str__(self):
        return str(self.username)




class bus(models.Model):
    # driver_id=models.IntegerField()
    name = models.CharField(max_length=300, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    driver = models.ForeignKey(driver, on_delete=models.CASCADE)




