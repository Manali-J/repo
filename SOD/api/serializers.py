from rest_framework import serializers
from . import models

class IMOSSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.IMOS
		fields = '__all__'
		
class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Environment
		fields = '__all__'