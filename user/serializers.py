from rest_framework import serializers
from .models import SoundUser
from django import forms, forms

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = SoundUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = SoundUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password'],
        )
        return user