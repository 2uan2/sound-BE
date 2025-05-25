from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    is_favourited = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = [
            'id', 'name', 'artist', 'file', 'duration', 'cover_image',
            'uploaded_at', 'uploaded_by', 'is_favourited'
        ]
        read_only_fields = ['uploaded_at', 'uploaded_by']

    def get_is_favourited(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return obj in user.favourite_songs.all()
        return False