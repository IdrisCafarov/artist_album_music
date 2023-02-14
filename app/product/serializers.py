from rest_framework import serializers
from product.models import *





class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Music
        fields='__all__'

class AlbumSerializer(serializers.ModelSerializer):

    musics = MusicSerializer(source='music', many=True,read_only=True)

    class Meta:
        model=Album
        fields=['id','name','artist','musics']


class ArtistSerializer(serializers.ModelSerializer):

    albums = AlbumSerializer(source='album', many=True,read_only=True)

    class Meta:
        model=Artist
        fields=['id','name','albums']



