from main.permissions import IsOwner
from main.serializers import SongSerializer
from .models import Song

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
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
    permission_classes = [IsOwner]
    