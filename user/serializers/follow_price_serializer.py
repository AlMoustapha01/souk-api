from rest_framework import serializers
from user.models.follow_price_model import *
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class FollowPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FollowPrice
        fields = '__all__'