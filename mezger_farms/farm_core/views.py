from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from farm_core.models import Farm
from farm_core.serializers import FarmSerializer


class FarmViewSet(ModelViewSet):

    serializer_class = FarmSerializer
    queryset = Farm.objects.all()
