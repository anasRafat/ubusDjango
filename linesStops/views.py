
from linesStops.models import Lines , Stations
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers


class linesSer (serializers.ModelSerializer) :
    class  Meta:
        model = Lines
        fields = "__all__"
        
        
class StationsSer (serializers.ModelSerializer) :
    class  Meta:
        model = Stations
        fields = "__all__"


class Linesview (APIView):
      def get(self,request):
            lines=Lines.objects.all()
            Lines_ser=linesSer(lines,many=True)
            return Response( Lines_ser.data)
 
        
class stationsview (APIView):
      def get(self,request):
            stations=Stations.objects.all()
            statins_ser=StationsSer(stations,many=True)
            return Response( statins_ser.data)
 
