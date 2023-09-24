from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    department = models.CharField(max_length=5)
    salary = models.IntegerField()
    status = models.BooleanField()

