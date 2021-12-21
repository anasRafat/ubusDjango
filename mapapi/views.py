
import jwt,datetime

from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.response import Response

@api_view(['POST'])
def create(request):
        ser = Mapser(data=request.data)
        if ser.is_valid():
             ser.save()
        return Response(ser.data)
           
@api_view(['POST'])
def update(request,name):
    maps = bus.objects.filter(name=name)
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
    maps = bus.objects.all()
    ser = Mapser(maps, many=True)
    return Response(ser.data)

# @api_view(['GET'])
# def drive_det(request,name):
#     maps = bus.objects.get(name=name)
#     ser = Mapser(maps, many=False)
#     return Response(ser.data)


@api_view(['DELETE'])
def drive_delete(request,name):
    maps = bus.objects.get(name=name)
    maps.delete()
    return Response("delete success")



@api_view(['POST'])
def register(request):
        ser = deiverser(data=request.data)
        if ser.is_valid():
             ser.save()
        return Response(ser.data)


# @api_view(['GET'])
# def driver_get(request):
#     maps = driver.objects.all()
#     ser = deiverser(maps, many=True)
#     return Response(ser.data)



class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = driver.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        elif(user.password==password):
            tokens = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow(),
                "username": user.username,
                "last_name": user.last_name,
                "first_name": user.first_name,
                "bus_number":user.bus_number

            }

            token = jwt.encode(tokens, 'secret', algorithm='HS256')

            response = Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token
            }
            return response








