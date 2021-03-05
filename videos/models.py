from django.db import models

# Create your models here.
class film(models.Model):
    movie_url = models.URLField(default=None)
    movie_name = models.CharField(default=None , max_length=50)
    movie_date = models.DateTimeField(auto_now=True)