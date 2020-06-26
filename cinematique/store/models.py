from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class bollywood(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    ratings = models.FloatField()
    watchat = models.CharField(max_length=60)
    link = models.URLField(max_length = 200) 
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name


class hollywood(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    ratings = models.FloatField()
    watchat = models.CharField(max_length=60)
    link = models.URLField(max_length = 200) 
    image = models.ImageField(null=True, blank=True)   
    def __str__(self):
        return self.name        


class Anime(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    ratings = models.FloatField()
    watchat = models.CharField(max_length=60 )
    link = models.URLField(max_length = 200) 
    image = models.ImageField(null=True, blank=True)
    seasons = models.IntegerField(default='1')
    def __str__(self):
        return self.name



class web(models.Model):
    name = models.CharField(max_length=60)
    year = models.IntegerField()
    ratings = models.FloatField()
    watchat = models.CharField(max_length=60)
    link = models.URLField(max_length = 200) 
    image = models.ImageField(null=True, blank=True)
    seasons = models.IntegerField(default='1')
    def __str__(self):
        return self.name