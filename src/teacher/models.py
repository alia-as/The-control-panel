from django.db import models

# Create your models here.
class teacher(models.Model):
    uploaded_videos = models.FileField(default=None)
    exercises = models.TextField(default=None)