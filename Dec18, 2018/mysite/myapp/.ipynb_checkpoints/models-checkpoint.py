from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    
