from django.db import models

# Create your models here.
class Employee(models.Model):
    gender_choices=(('male','MALE'),('female','FEMALE'))
    empid=models.IntegerField(unique=True)
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    joining_date=models.DateField(auto_now_add=True)

    image=models.ImageField(upload_to="Employee",null=True)