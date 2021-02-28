from django.db import models

# Create your models here.
class student(models.Model):
    name            = models.CharField(max_length=100 , default=None)
    email           = models.EmailField(default=None, null=True, blank=True)
    student_number  = models.DecimalField(decimal_places=0 , max_digits=9 , default=000000000)