from django.shortcuts import render
from user.models.user_model import *
from user.serializers.user_serializer import *
from rest_framework.response import Response
from rest_framework import mixins,views
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from djoser.email import ActivationEmail,ConfirmationEmail,PasswordResetEmail,PasswordChangedConfirmationEmail,UsernameChangedConfirmationEmail,UsernameResetEmail
from rest_framework.settings import api_settings
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
class UsersView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class= UsersSerializer
    queryset = Users.objects.all()
    lookup_field='id'

    def get(self,request):
        return self.list(request)

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user=Users.objects.get(email=serializer.data['email'])
        current_site=get_current_site(request).domain
        link= reverse('v1/users/activation/')
        data={'domain': current_site}
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class UsersViewById(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class= UsersSerializer
    queryset = Users.objects.all()

    lookup_field='id'

    def get(self,request,id=None):
        return self.retrieve(request)

    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)