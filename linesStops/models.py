from django.db import models
from django.db import models


class Lines (models.Model) : 
    line = models.CharField(max_length=50)
    
class Stations (models.Model) : 
    st_latitude=models.IntegerField()
    st_longitude=models.IntegerField ()
    station = models.CharField(max_length=50)
    line =  models.ForeignKey(Lines, on_delete=models.CASCADE)
