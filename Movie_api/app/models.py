from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=30)
    year=models.IntegerField()
    runtime=models.IntegerField()
    language=models.CharField(max_length=20)
    rating=models.FloatField()