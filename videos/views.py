from django.shortcuts import render
from .models import video
from .forms import upload_form
# Create your views here.

def upload_view(request):
    form = upload_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = upload_form()
    return render(request,"upload_temp.html",{'form' : form})
def video_view(request):
    return render(request,"video_temp.html",{})