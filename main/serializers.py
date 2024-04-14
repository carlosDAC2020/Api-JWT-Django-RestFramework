from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","title","status","description","user"]