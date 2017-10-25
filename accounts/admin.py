# -*- coding: utf-8 -*-

from django.contrib import admin


# Register your models here.
from django.contrib.admin import forms
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm

from accounts.models import BaseUser


class UserCreationForm(ModelForm):
    class Meta:
        model = BaseUser
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)
    list_filter = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_superuser',)}
            ),
        )

    fieldsets = (
        ('User Info', {
            'fields': (
                'email', 'password',
                ('first_name', 'last_name',),
            ),
        }),
        ('Roles', {
            'fields': (
                'is_superuser',
                'groups',
            ),
        }),
    )

    filter_horizontal = ()


admin.site.register(BaseUser, CustomUserAdmin)
