from django.shortcuts import render
from .models import teacher
from .teacher_form import teacher_form
# Create your views here.
def teacherview(request,*args,**kwargs):
    form = teacher_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = teacher_form
    context = {'form' : form}
    return render(request,"teacher_temp.html",context)