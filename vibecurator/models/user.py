from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    spotify_data = models.JSONField()
    apple_music_data = models.JSONField()
