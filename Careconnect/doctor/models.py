from django.db import models

class Doctor(models.Model):
    specialization_options = (
        ("cardiology", "Cardiology"),
        ("dermatology", "Dermatology"),
        ("endocrinology", "Endocrinology"),
        ("ent", "Ear, Nose & Throat (ENT)"),
        ("gastroenterology", "Gastroenterology"),
        ("generalmedicine", "General Medicine / Internal Medicine"),
        ("general_surgery", "General Surgery"),
        ("gynecology", "Gynecology & Obstetrics"),
        ("hematology", "Hematology"),
        ("nephrology", "Nephrology"),
        ("neurology", "Neurology"),
        ("oncology", "Oncology"),
        ("ophthalmology", "Ophthalmology"),
        ("orthopedics", "Orthopedics"),
        ("pediatrics", "Pediatrics"),
        ("psychiatry", "Psychiatry"),
        ("pulmonology", "Pulmonology"),
        ("radiology", "Radiology"),
        ("urology", "Urology"),
        ("other", "Other"),
    )
    name=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20,choices=specialization_options)
    fee=models.IntegerField()
    qualification=models.CharField(max_length=30)
    email=models.CharField(max_length=50)