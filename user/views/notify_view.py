from django.shortcuts import render
from user.models.notify_model import *
from user.serializers.notify_serializer import *
from rest_framework.response import Response
from rest_framework import mixins,views
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)

class NotifyView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class= NotifySerializer
    queryset = Notify.objects.all()
    lookup_field='id'

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class NotifyViewById(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class= NotifySerializer
    queryset = Notify.objects.all()

    lookup_field='id'

    def get(self,request,id=None):
        return self.retrieve(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)