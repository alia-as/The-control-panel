from django import forms
from .models import video

class upload_form(forms.ModelForm):
    class Meta:
        model = video
        fields = [
            'the_video',
        ]