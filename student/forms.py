from django import forms
from .models import student

class stu_add_form(forms.ModelForm):
    class Meta:
        model = student
        fields = ["student_number",
                  "username",
                  "first_name",
                  "email",
                  "password",]