from rest_framework import serializers
from comparator.models.product_model import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

