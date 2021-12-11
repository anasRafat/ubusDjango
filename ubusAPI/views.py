from django.shortcuts import render
# Create your views here.
from ubusAPI.serializer import BusesSer, RoutesSer, StationesSer, DriverSer, RoutesStationSer, UserTicketSer
from ubusAPI.models import Buses, Routes, Stationes, Driver, RoutesStation, UserTicket
from rest_framework import generics


class RoutesAPI(generics.ListAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSer

class StationAPI(generics.ListAPIView):
    queryset = Stationes.objects.all()
    serializer_class = StationesSer

class BusAPI(generics.ListAPIView):
    queryset = Buses.objects.all()
    serializer_class = BusesSer

class DriverAPI(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSer

class RoutesStationAPI(generics.ListAPIView):
    queryset = RoutesStation.objects.all()
    serializer_class = RoutesStationSer


class UserTicketAPI(generics.ListAPIView):
    queryset = UserTicket.objects.all()
    serializer_class = UserTicketSer

