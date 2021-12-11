from rest_framework import serializers
from ubusAPI import models


class RoutesSer(serializers.ModelSerializer):
    class Meta:
        model = models.Routes
        fields = '__all__'


class StationesSer(serializers.ModelSerializer):
    class Meta:
        model = models.Stationes
        fields = '__all__'


class BusesSer (serializers.ModelSerializer):
    class Meta:
        model = models.Buses
        fields = '__all__'


class DriverSer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'

class RoutesStationSer (serializers.ModelSerializer):
    class Meta:
        model = models.RoutesStation
        fields = '__all__'

class UserTicketSer (serializers.ModelSerializer):
    class Meta:
        model = models.UserTicket
        fields = '__all__'
