from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'username']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
