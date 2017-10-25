# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


# Create your models here.
class EmailUserManager(BaseUserManager):
    def _create_user(self, email, password=None, is_superuser=False, **kwargs):
        user = self.model(email=email, is_superuser=is_superuser, **kwargs)
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        return self._create_user(email, password, is_superuser=False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, is_superuser=True, **kwargs)

    def get_by_natural_key(self, email):
        return self.get(email__iexact=email)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=False)

    objects = EmailUserManager()
    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_superuser

    def get_full_name(self):
        """Returns first_name plus last_name, with a space in between."""
        full_name = '{} {}'.format(self.first_name, self.last_name).strip()
        return full_name or self.email

    def get_short_name(self):
        """Returns the short name for the User."""
        return self.first_name or self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

