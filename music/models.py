from django.db import models

# migrations only needed when changing columns

# Create your models here.
class Album(models.Model):
    # var names are columns
    # max length is char length
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_logo = models.CharField(max_length=1000)

    # for displaying data in table
    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=200)
    song_title = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title

