from rest_framework import serializers
from comparator.models.site_model import *

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

