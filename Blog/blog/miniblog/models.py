from django.db import models

# Create your models here.

class Postblog(models.Model):

    title= models.CharField(max_length=200)
    desc= models.TextField()


class Comment(models.Model):
    name=models.CharField(max_length=50)    
    email=models.EmailField()
    comments=models.TextField()