from rest_framework import serializers 
from core.models import MedPMGV

class MedPMGVSerializer(serializers.ModelSerializer):

	class Meta:
		model = MedPMGV
		fields = '__all__'