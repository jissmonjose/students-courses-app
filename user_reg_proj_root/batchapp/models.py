from django.db import models
from courseapp.models import CourseModel


# Create your models here.
class Batch(models.Model):
    batch_number = models.CharField(max_length=20)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.batch_number
