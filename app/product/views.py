from django.shortcuts import render
from rest_framework import viewsets
from product.models import *
from product.serializers import *
from rest_framework.response import Response

# Create your views here.



class ArtistCreateView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer



class AlbumCreateView(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer



class MusicCreateView(viewsets.ModelViewSet):
    serializer_class = MusicSerializer




#############################################################################

class ArtistListView(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumListView(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class MusicListView(viewsets.ModelViewSet):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

