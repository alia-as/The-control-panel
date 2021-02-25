from django.db import models

# Create your models here.
class exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=5 , decimal_places=2)
class student_exer(exercise):
    pass
class teacher_exer(exercise):
    pass