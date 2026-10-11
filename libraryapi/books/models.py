from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=40)
    author=models.CharField(max_length=40)
    language=models.CharField(max_length=30)
    price=models.IntegerField()
    pages=models.IntegerField()
    image=models.ImageField(upload_to="books",null=True)

