from django import forms
from .models import teacher

class teacher_form(forms.ModelForm):
    class Meta:
        model = teacher
        fields = [
            "uploaded_videos",
            "exercises"
        ]