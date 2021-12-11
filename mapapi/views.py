from rest_framework.views import APIView
from map.models import measurement
from .serializers import Mapser
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status

# Create your views here.

class mapview(APIView):
    def get(self, request):
        maps = measurement.objects.all()
        ser = Mapser(maps, many=True)
        return Response(ser.data)

