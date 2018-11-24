from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'imos', views.IMOSViewSet)

urlpatterns = [
	path('', include('rest_auth.urls')),
]

urlpatterns += router.urls