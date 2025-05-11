from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# from main.models import Song

class SoundUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    favourite_songs = models.ManyToManyField('main.Song', blank=True, related_name="favourited_by")
     
    def __str__(self):
        return self.username
    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)