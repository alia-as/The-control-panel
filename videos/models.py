from django.db import models

# Create your models here.
class film(models.Model):
    movie = models.FileField(default=None , null=True, blank=True)