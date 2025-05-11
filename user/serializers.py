from rest_framework import serializers

from main.serializers import SongSerializer
from .models import SoundUser
from django import forms, forms

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    favourite_songs = serializers.SerializerMethodField()

    class Meta:
        model = SoundUser
        fields = ['username', 'email', 'password', 'favourite_songs']

    def get_favourite_songs(self, obj):
        # serializer = SongSerializer(obj.songs.filter(favourited=True))
        # print(serializer.data)
        song_ids = []
        for song in obj.songs.filter(favourited=True):
            song_ids.append(song.id)
        return song_ids
 
    def create(self, validated_data):
        user = SoundUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password = validated_data['password'],
        )
        return user