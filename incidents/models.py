import email
from django.db import models

# Create your models here.



class Incident(models.Model):
    location1=models.CharField(max_length=600)
    location2=models.CharField(max_length=600)
    description=models.CharField(max_length=900)
    date=models.DateField(max_length=300)
    time=models.TimeField(max_length=300)
    severity=models.CharField(max_length=300)
    cause=models.CharField(max_length=900)
    actions=models.CharField(max_length=900)
    type_env=models.CharField(max_length=200)
    type_inju=models.CharField(max_length=200)
    type_property=models.CharField(max_length=200)
    type_vehicle=models.CharField(max_length=200)
    
    reported_by=models.CharField(max_length=900)   
    submitted=models.CharField(max_length=200, default='f')    

    def __str__(self):
        return self.name