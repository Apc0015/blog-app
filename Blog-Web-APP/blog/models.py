from django.db import models
from django.urls import reverse
# Create your models here.
class art(models.Model):
    title = models.CharField(max_length=30)
    text= models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
