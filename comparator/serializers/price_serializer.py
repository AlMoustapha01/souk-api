from rest_framework import serializers
from comparator.models.price_model import *

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

