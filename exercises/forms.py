from django import forms
from .models import exercise

class exercise_form(forms.ModelForm):
    class Meta:
        model = exercise
        fields = ['exercise_name' , 'grade']