from django.db import models

# Create your models here.
class Hashtag(models.Model):
    title = models.CharField(max_length=10)





class Post(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()
    image = models.ImageField()
    likes = models.IntegerField()
    hashtag = models.ManyToManyField(Hashtag, null=True)