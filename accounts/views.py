# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import uuid

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework import viewsets

# Create your views here.
from accounts.forms import BaseUserCreationForm
from accounts.models import BaseUser
from accounts.serializers import UserSerializer, ReadUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.none()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadUserSerializer
        return UserSerializer


def signup(request):
    if request.method == 'POST':
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = BaseUserCreationForm()
    return render(request, 'signup.html', {'form': form})