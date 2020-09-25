from django.db import models
from django.urls import reverse

# Create your models here.


class Widget(models.Model):
    Description = models.CharField(max_length=50)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('index')
