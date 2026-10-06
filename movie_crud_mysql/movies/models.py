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