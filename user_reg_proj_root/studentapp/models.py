from django.db import models
from courseapp.models import CourseModel
from batchapp.models import Batch
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50, unique=True)
    select_course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    select_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
