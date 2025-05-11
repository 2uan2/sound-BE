from django.db import models

from user.models import SoundUser

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to="songs/", null=True, blank=True)
    duration = models.IntegerField()
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(SoundUser, on_delete=models.SET_NULL, related_name="songs", null=True, blank=True)
    favourited = models.BooleanField(default=False)

    def __str__(self):
        return self.name

