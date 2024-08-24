from rest_framework import serializers
from .models import Planes


class PlanesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = '__all__'
