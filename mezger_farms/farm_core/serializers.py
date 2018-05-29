from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from farm_core.models import Farm


class FarmSerializer(ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Farm
        fields = '__all__'
