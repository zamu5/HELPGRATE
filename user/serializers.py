from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)
        model = User
