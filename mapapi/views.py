
from rest_framework.decorators import api_view

from .models import driver
from .serializers import Mapser
from rest_framework.response import Response

@api_view(['POST'])
def create(request):
        ser = Mapser(data=request.data)
        if ser.is_valid():
             ser.save()
        return Response(ser.data)
           
@api_view(['POST'])
def update(request,name):
    maps = driver.objects.filter(name=name)
    if not maps:
        ser = Mapser(data=request.data)
        if ser.is_valid():
            print("valid")
            ser.save()
        return Response(ser.data)
    maps.update(latitude=request.data["latitude"], longitude=request.data["longitude"])
    return Response(200)

@api_view(['GET'])
def drive_get(request):
    maps = driver.objects.all()
    ser = Mapser(maps, many=True)
    return Response(ser.data)

@api_view(['GET'])
def drive_det(request,name):
    maps = driver.objects.get(name=name)
    ser = Mapser(maps, many=False)
    return Response(ser.data)