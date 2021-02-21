from django import forms
from .models import video

class video_uploading_form(forms.ModelForm):
    class Meta:
        model = video
        fields = ['video_name']