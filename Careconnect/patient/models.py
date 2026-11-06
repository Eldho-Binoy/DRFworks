from django.db import models

# Create your models here.
class Patient(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    doctor=models.
    appointment_time=models.TimeField()
    appointment_date=models.DateField()
    token_number=models.IntegerField()