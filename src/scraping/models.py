from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)
    slag = models.CharField(max_length=50,blank=True)

