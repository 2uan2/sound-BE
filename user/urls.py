from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
    path('', views.TestView.as_view(), name='test'),
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
]