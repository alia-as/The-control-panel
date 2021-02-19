from django.db import models

# Create your models here.
class student(models.Model):
    videos_to_watch = models.TextField()
    exercises = models.TextField()