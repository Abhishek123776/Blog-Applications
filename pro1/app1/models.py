from django.db import models

# Create your models here.

class Post(models.Model):
    post_id=models.IntegerField()
    post_name=models.CharField(max_length=50)
    post_income=models.FloatField()

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comments=models.TextField()
    rating=models.IntegerField()
