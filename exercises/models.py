from django.db import models

# Create your models here.
class exercise(models.Model):
    exercise_name = models.CharField(max_length=100 , null=True , blank=True)
    grade         = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    exercise_file = models.FileField(default=None , null=True , blank=True)
    date          = models.DateField(auto_now=True)