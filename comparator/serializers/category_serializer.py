from rest_framework import serializers
from comparator.models.category_model import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

