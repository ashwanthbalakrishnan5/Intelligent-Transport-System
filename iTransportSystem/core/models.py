from django.db import models


# Create your models here.
class Transport(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    route = models.CharField(max_length=50)
