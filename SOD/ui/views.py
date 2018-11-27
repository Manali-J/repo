from django.shortcuts import render
from django.views.generic import ListView
#from . import models
from api import models

class HomeView(ListView):
	template_name = 'ui/home.html'
	queryset = models.IMOS.objects.all()