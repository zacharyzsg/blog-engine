# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from accounts.models import BaseUser
from accounts.serializers import UserSerializer, ReadUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.none()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadUserSerializer
        return UserSerializer
