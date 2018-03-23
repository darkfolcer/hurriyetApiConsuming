from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Paths(models.Model):
    _Id = models.CharField(max_length = 100)
    Path = models.CharField(max_length = 200)
    Title = models.CharField(max_length = 200)

    def __str__(self):
        return self.Title
class userPreferences(models.Model):
    email = models.CharField(max_length = 150)
    Title = models.CharField(max_length = 600)
    categoryId = models.CharField(max_length = 100)
    Path = models.CharField(max_length = 300)

class Article(models.Model):
     _Id = models.CharField(max_length = 100)
     description = models.CharField(max_length=2000)
     url = models.CharField(max_length=400)
     img = models.CharField(max_length=600)
     tittle = models.CharField(max_length=600)

     def __str__ (self):
         return self.tittle

class Path(models.Model):
    _Id = models.CharField(max_length = 100)
    Path = models.CharField(max_length = 300)
    Tittle = models.CharField(max_length=600)

class Articles(models.Model):
    Id = models.CharField(max_length = 100)
    Path = models.CharField(max_length = 300)
    url = models.CharField(max_length=400)
    img = models.CharField(max_length=600)
    tittle = models.CharField(max_length=600)
    description = models.CharField(max_length=2000)
    def __str__(self):
        return self.Id