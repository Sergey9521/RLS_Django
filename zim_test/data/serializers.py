from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ['firm', 'data_name', 'data_check']
