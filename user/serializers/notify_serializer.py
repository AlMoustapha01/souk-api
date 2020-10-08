from rest_framework import serializers
from user.models.notify_model import *
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class NotifySerializer(serializers.ModelSerializer):

    class Meta:
        model = Notify
        fields = '__all__'