from django import forms
from .models import stu_exercise , tea_exercise

class exercise_form_tea(forms.ModelForm):
    class Meta:
        model = tea_exercise
        fields = ['exercise_name' ,]
class exercise_form_stu(forms.ModelForm):
    class Meta:
        model = stu_exercise
        fields = ['exercise_file' ,]
class exercise_form_tea_grade(forms.ModelForm):
    class Meta:
        model = tea_exercise
        fields = ['grade' ,]