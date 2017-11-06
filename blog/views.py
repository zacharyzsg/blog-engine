# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from rest_framework import viewsets

from blog.models import Post, Comment


@login_required
def home(request):
    return render(request, 'home.html')
