from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    x = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=50)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField()
