from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=128)
    joined = models.DateField()
