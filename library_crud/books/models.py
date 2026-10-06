from django.db import models

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    pages=models.IntegerField()
