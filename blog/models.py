from django.db import models

# Create your models here.

class Post(models.Models):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    short_description = models.CharField(max_length=100, blank=True, null=True)
    likes_of_amount = models.CharField(max_length=3, choices=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)