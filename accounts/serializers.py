from rest_framework import serializers
from accounts import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Accounts
        fields = '__all__'
