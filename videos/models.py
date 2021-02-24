from django.db import models

# Create your models here.
class film(models.Model):
    movie = models.CharField(max_length=20)