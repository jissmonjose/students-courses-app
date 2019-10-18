from django.db import models
from batchapp.models import Batch


class ClassRoom(models.Model):
    classroom = models.CharField(max_length=5)

    def __str__(self):
        return self.classroom


class TimeTable(models.Model):
    select_batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.select_batch}'s Schedule"
