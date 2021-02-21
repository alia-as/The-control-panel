from django import forms
from .models import video

class video_uploading(forms.ModelForm):
    class meta:
        model = video
        fields = ['name']