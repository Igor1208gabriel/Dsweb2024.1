from django.db import models

# Create your models here.

class Remedio(models.Model):
    tomou = models.BooleanField(default=False)