from rest_framework import serializers
from comparator.models.lowcategory_model import *

class LowCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LowCategory
        fields = '__all__'

