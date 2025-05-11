from django.shortcuts import get_object_or_404
from main.permissions import IsOwner
from main.serializers import SongSerializer
from user.models import SoundUser
from user.serializers import UserSerializer
from .models import Song

from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
    
# class SongViewSet(viewsets.ModelViewSet):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
#     permission_classes = [IsAuthenticated]

class SongList(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request)
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("serializer: ", serializer)
        return serializer.save(uploaded_by=self.request.user)
        # return super().perform_create(serializer)

class SongDetail(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated] #IsOwner


class FavouriteSongDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = SoundUser.objects.get(pk=request.user.pk)
        instance = get_object_or_404(Song, pk=pk)
        print(instance)
        print(user)
        # serializer = SongSerializer(data=instance)
        # serializer.is_valid(raise_exception=True)
        print(user.favourite_songs.all())
        if instance in user.favourite_songs.all():
            print(f'{instance.pk} in {user.favourite_songs.all()}')
            user.favourite_songs.remove(instance)
            return Response({f"succesfully removed song with id {instance.pk}"})
            # user.favourite_songs.save()
        else:
            print(f'{instance.pk} not in {user.favourite_songs.all()}')
            user.favourite_songs.add(instance)
            return Response({f"succesfully added song with id {instance.pk}"})
            # user.favourite_songs.save()
        # user.favourite_songs.add(serializer.data.pk)
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)




        