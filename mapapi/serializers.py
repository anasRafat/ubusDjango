from rest_framework import serializers
from map.models import measurement


class Mapser(serializers.ModelSerializer):
    class Meta:
        model = measurement
        fields = '__all__'