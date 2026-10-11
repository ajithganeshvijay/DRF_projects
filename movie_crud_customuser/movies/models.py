from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=40)
    director=models.CharField(max_length=40)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    rating=models.FloatField()
    run_time=models.IntegerField()
    image=models.ImageField(upload_to="movies",null=True)

class MyUser(AbstractUser):
    phone=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=20,null=True)