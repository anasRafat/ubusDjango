from rest_framework import serializers
from .models import driver


class Mapser(serializers.ModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'