from django.db import models

# Create your models here.

class Exercise(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 200)
    theme = models.CharField(max_length = 100)
    options = models.CharField(max_length = 450)
    rightAns = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(primary_key = True, max_length = 50)
    password = models.TextField(default = 'qwerty12')
    def __str__(self):
        return self.username
