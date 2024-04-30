from django.db import models
from .user import User

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.JSONField()