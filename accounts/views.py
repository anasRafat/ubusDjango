from django.shortcuts import render
from accounts.models import Accounts
from accounts.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# Create your views here.


class UsersAPI(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_user(self):
        user = self.request.user
        return user
