# serializers.py
from rest_framework import serializers
from .models import Alcohol

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = '__all__'