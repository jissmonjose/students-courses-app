from django.db import models
from trainers.models import TrainerModel
from django.urls import reverse


# Create your models here.

class CourseModel(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    fees = models.IntegerField()
    trainer = models.ForeignKey(TrainerModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('course_update', kwargs={'pk': self.pk})
