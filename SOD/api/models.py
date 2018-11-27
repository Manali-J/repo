from django.db import models



class Environment(models.Model):
	environment = models.CharField(max_length = 10, unique = True)
	
	def __str__(self):
		return self.environment

class IMOS(models.Model):
	lob = models.CharField(max_length = 30)
	seal_id = models.IntegerField(unique = True)
	application_name = models.CharField(max_length = 100)
	environment = models.ForeignKey(Environment, on_delete = models.CASCADE, default = 0)
	details = models.TextField(blank = True)
	status = models.CharField(max_length = 20, choices = (("Green", "Green"), ("Yellow", "Yellow"), ("Red", "Red"), ("Grey", "Grey")), default = "Green")
