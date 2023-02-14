from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=25, verbose_name="Artist Name")


    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=30, verbose_name="Album Name")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="album")

    def __str__(self):
        return self.name



class Music(models.Model):
    name = models.CharField(max_length=30, verbose_name="Music Name")
    album = models.ManyToManyField(Album, related_name='music')

    def __str__(self):
        return self.name
