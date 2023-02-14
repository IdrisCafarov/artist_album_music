from django.urls import path
from .views import *

urlpatterns = [

    path("create_artist/", ArtistCreateView.as_view({
    'post': 'create'
    }), name="create_artost"),

    path("create_album/", AlbumCreateView.as_view({
    'post': 'create'
    }), name="create_album"),

    path("create_music/", MusicCreateView.as_view({
    'post': 'create'
    }), name="create_music"),

    #####################################

    path("artist_list/", ArtistListView.as_view({
    'get': 'list',
    }), name="artist_list"),

    path("album_list/", AlbumListView.as_view({
    'get': 'list',
    }), name="album_list"),

    path("music_list/", MusicListView.as_view({
    'get': 'list',
    }), name="music_list"),


]
