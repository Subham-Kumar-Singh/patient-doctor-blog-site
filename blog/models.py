from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.AutoField(primary_key=True)
    image=models.ImageField(null=True,blank=True)
    image=models.ImageField(default="my.jpeg",null=True,blank=True)
    category=models.CharField(max_length=50)
    summary=models.CharField(max_length=100)
    Content=models.CharField(max_length=2000)
    
