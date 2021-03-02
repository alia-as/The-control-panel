from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student(models.Model):
    username            = models.CharField(max_length=100 , default=" ")
    first_name          = models.CharField(max_length=100, default=None)
    email               = models.EmailField(default=None, null=True, blank=True)
    student_number      = models.DecimalField(decimal_places=0 , max_digits=9 , default=000000000)
    password            = models.CharField(max_length=50 , default=None , null=True)