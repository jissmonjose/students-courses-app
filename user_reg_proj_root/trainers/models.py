from django.db import models
from PIL import Image
from django.shortcuts import reverse


# Create your models here.
class TrainerModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    experience = models.TextField(default='blah')
    photo = models.ImageField(upload_to='photos', default='default.jpg')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(TrainerModel, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.photo.path)

    def get_absolute_url(self):
        return reverse('trainer_one', kwargs={'pk': self.pk})
