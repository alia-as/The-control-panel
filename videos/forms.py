from django import forms
from .models import film

class film_form(forms.ModelForm):
    class Meta:
        model = film
        fields = ['movie']
    def clean_name(self,*args,**kwargs):
        the_movie = self.cleaned_data.get("title")
        if "mkv" in the_movie:
            return the_movie
        else:
            raise forms.ValidationError("It must be mkv movie")
class upload_form(forms.Form):
    title = forms.CharField(max_length=50)
    video = forms.FileField()