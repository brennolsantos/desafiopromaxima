from django.urls import path, include
from core.api import MedPMGVAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'medpmgv', MedPMGVAPI)


app_name='core'

urlpatterns = [
	path('', include(router.urls))	
]
