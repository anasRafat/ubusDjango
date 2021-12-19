
from django.db import models

class driver(models.Model):
    # driver_id=models.IntegerField()
    name=models.CharField(max_length=300,unique=True)
    latitude=models.FloatField()
    longitude=models.FloatField()