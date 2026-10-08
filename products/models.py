from django.db import models

# Create your models here.

class Products(models.Model):

    name = models.CharField(max_length=60)

    price = models.FloatField()

    count = models.IntegerField()

    desciption = models.CharField(max_length=500)