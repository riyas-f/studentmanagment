from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=200)

class Student(models.Model):
    registration_number = models.CharField(max_length=200, null=True,default=None)
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  
        if not self.registration_number:
            id_start = 100000
            self.registration_number = 'IET' + str(self.id + id_start).zfill(6)
            super().save(update_fields=['registration_number'])
