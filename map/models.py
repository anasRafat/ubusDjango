from django.db import models


# Create your models here.

class measurement(models.Model):
    location =models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=10 ,decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Detance from {self.location} to {self.destination} is {self.distance} km"


# Create your models here.
