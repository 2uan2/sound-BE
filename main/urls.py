from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ExampleClass.as_view(), name="test"),
    path("", views.SongList.as_view(), name="song"),
    path("<int:pk>/", views.SongDetail.as_view(), name="song_detail"),
    path("<int:pk>/favourite/", views.FavouriteSongDetail.as_view(), name="favourite"),
    # path('example', views.RegistrationView.as_view(), name="example"),
    # Artist endpoints
    path("artists/", views.ArtistList.as_view(), name="artist-list"),
    path("artists/<int:pk>/", views.ArtistDetail.as_view(), name="artist-detail"),
    path("artists/<int:artist_id>/songs/", views.SongsByArtist.as_view(), name="songs-by-artist"),
]
