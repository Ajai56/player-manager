from django.db import models

class player(models.Model):
    player_name = models.CharField(max_length=100)
    player_age = models.IntegerField()
    player_number = models.IntegerField()

    def __str__(self):
        return self.player_name

# Create your models here.
