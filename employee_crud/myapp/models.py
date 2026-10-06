from django.db import models

# Create your models here.
class Employee(models.Model):
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender_choice=[
        ('male','Male'),('female','Female') #('DB value','display value')
    ]
    gender=models.CharField(max_length=20,choices=gender_choice)
    salary=models.IntegerField()
    joining_date=models.DateField()
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images",null=True)