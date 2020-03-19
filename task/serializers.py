from django.contrib.auth.models import User
from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['topic', 'title', 'description']
        model = Task


class TaskHelperSerializer(serializers.ModelSerializer):
    helper = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = ['helper']
        model = Task


class HelperSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'first_name',
            'last_name',
            'id',
        ]
        model = User


class TaskSerializerDetail(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d / %H:%M:%S')
    owner = serializers.StringRelatedField(many=True)
    topic = serializers.StringRelatedField()
    helper = HelperSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Task
