from django.db import models


class IMOS(models.Model):
	lob = models.CharField(max_length = 30)
	seal_id = models.IntegerField(unique = True)
	application_name = models.CharField(max_length = 100)
	environment = models.CharField(max_length = 100)
	details = models.TextField(blank = True)
	



