from . import models
from rest_framework import viewsets
from rest_framework import generics
from api.serializers import IMOSSerializer, EnvironmentSerializer

class IMOSViewSet(viewsets.ModelViewSet):
	queryset = models.IMOS.objects.all()
	serializer_class = IMOSSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
	queryset = models.Environment.objects.all()
	serializer_class = EnvironmentSerializer