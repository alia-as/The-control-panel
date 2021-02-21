from django.db import models

# Create your models here.
class video(models.Model):
    the_video = models.FileField(default=None)