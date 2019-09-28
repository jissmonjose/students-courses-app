from django.db import models


# Create your models here.
class TrainerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
