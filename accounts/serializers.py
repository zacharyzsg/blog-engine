from rest_framework import serializers
from accounts.models import Organization, BaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        exclude = ('password', )
