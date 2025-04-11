from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ExampleClass.as_view(), name="test"),
    path('', views.SongList.as_view(), name="song"),
    path('<int:pk>/', views.SongDetail.as_view(), name="song_detail"),
    # path('example', views.RegistrationView.as_view(), name="example"),
]