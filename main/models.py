from django.db import models


from user.models import SoundUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)
    avatar = models.ImageField(upload_to="artist_images/", default="default/faker1.jpg")

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    artist_fk = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)  # new field

    file = models.FileField(upload_to="songs/", null=True, blank=True)
    duration = models.IntegerField()
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(SoundUser, on_delete=models.SET_NULL, related_name="songs", null=True, blank=True)
    # favourited = models.BooleanField(default=False)

    def __str__(self):
        return self.name



@receiver(post_save, sender=Song)
def create_artist_if_not_exists(sender, instance, created, **kwargs):
    if instance.artist:  # even if not newly created, allow fix
        artist_obj, _ = Artist.objects.get_or_create(name=instance.artist)
        if instance.artist_fk != artist_obj:
            instance.artist_fk = artist_obj
            instance.save(update_fields=["artist_fk"])