from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title




class Post(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()
    likes = models.IntegerField()
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.author}: {self.text}'