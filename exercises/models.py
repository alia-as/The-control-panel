from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
class exercise(models.Model):
    exercise_name       = models.CharField(max_length=100 , null=True , blank=True)
    description         = models.CharField(max_length=1000 , null=True , blank=True)
    exp_date            = models.DateField(default=None)
    grade               = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    exercise_file       = models.URLField(default=None , null=True , blank=True)
    exercise_file_name  = models.CharField(default=None , null=True , blank=True,  max_length=50)
    date                = models.DateField(auto_now=True)
    def get_absolute_url(self):
        return reverse("teacher-exercise",kwargs={'id' : self.id})
class tea_exercise(exercise):
    uploaded_student = []
class stu_exercise(exercise):
    is_uploaded = models.BooleanField(default=False)