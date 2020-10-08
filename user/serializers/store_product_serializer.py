from rest_framework import serializers
from user.models.store_product_model import *

class StoreProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreProduct
        fields = '__all__'