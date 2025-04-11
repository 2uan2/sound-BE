from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'#['name', 'artist', 'duration']
        read_only_fields = ['uploaded_at', 'uploaded_by']

    def create(self, validated_data):
        # validated_data
        return super().create(validated_data)

