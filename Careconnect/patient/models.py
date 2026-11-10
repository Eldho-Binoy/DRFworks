from django.db import models
from doctor.models import Doctor

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_time=models.TimeField(null=True)
    appointment_date=models.DateField(null=True)
    token_number=models.IntegerField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,null=True)