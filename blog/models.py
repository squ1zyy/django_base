from django.db import models

# Create your models here.

class Post(models.Models):
    title = models.CharField(max_length=200, )