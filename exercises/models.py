from django.db import models
from django.urls import reverse
# Create your models here.
class exercise(models.Model):
    exercise_name = models.CharField(max_length=100 , null=True , blank=True)
    grade         = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    exercise_file = models.CharField(default=None , null=True , blank=True , max_length=100)
    date          = models.DateField(auto_now=True)
    def get_absolute_url(self):
        return reverse("teacher-exercise",kwargs={'id' : self.id})
class tea_exercise(exercise):
    uploaded_student = []
class stu_exercise(exercise):
    is_uploaded = models.BooleanField(default=False)