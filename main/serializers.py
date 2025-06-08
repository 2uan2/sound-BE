from rest_framework import serializers
from .models import Song
from .models import Artist


class SongSerializer(serializers.ModelSerializer):
    is_favourited = serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()
    artist_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = [
            "id",
            "name",
            "artist",
            "artist_name",
            "artist_avatar",
            "file",
            "duration",
            "cover_image",
            "uploaded_at",
            "uploaded_by",
            "is_favourited",
        ]
        read_only_fields = ["uploaded_at", "uploaded_by"]

    def get_is_favourited(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return obj in user.favourite_songs.all()
        return False

    def get_artist_name(self, obj):
        return obj.artist_fk.name if obj.artist_fk else obj.artist

    def get_artist_avatar(self, obj):
        request = self.context.get("request")
        if obj.artist_fk and obj.artist_fk.avatar:
            return request.build_absolute_uri(obj.artist_fk.avatar.url)
        return None


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name", "avatar"]
