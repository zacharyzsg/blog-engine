# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey('accounts.BaseUser')
    created_at = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey('accounts.BaseUser')
    post = models.ForeignKey(Post)
    content = models.TextField()
