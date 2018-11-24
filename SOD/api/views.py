from . import models
from rest_framework import viewsets
from rest_framework import generics
from api.serializers import IMOSSerializer

class IMOSViewSet(viewsets.ModelViewSet):
	queryset = models.IMOS.objects.all()
	serializer_class = IMOSSerializer

