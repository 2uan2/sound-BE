from user.serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from .models import SoundUser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class UserProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = SoundUser.objects.get(pk=request.user.pk)
        serializer = UserSerializer(user)
        print(serializer)
        return Response(serializer.data)

class RegistrationView(CreateAPIView):
    queryset = SoundUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print('serialzier', serializer)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print("user", user)

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'user': serializer.data,
            'username': user.username,
            'email': user.email,
            'token': token.key
        }, status=status.HTTP_201_CREATED)

        return super().create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     print('perform_create-d', serializer.validated_data)
    #     serializer.perform_create(serializer)
    #     serializer.validated_data['token'] = Token.objects.get(user=serializer.instance).key
    #     return Response(serializer.validated)
    
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # perform_create
    #     return Response(serializer.data, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # print(serializer.validated_data["user"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
        })
    
class TestView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
