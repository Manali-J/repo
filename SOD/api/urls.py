from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'imos', views.IMOSViewSet)
router.register(r'environment', views.EnvironmentViewSet)

urlpatterns = [
	path('', include('rest_framework.urls')),
]

urlpatterns += router.urls