from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3)
    colour = models.CharField(max_length=50)
