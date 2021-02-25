from django.shortcuts import render
from .forms import exercise_form
from .models import exercise
# Create your views here.

def stu_exer_view(request , *args,**kwargs):
    all_exer = exercise.objects.all()
    return render(request,"stexer_temp.html",{"all" : all_exer})
def tea_exer_view(request,*args,**kwargs):
    exer = exercise_form()
    if request.method == "POST":
        exer = exercise_form(request.POST)
        if exer.is_valid():
            exer.save()
            exer = exercise_form()
        else:
            print('Errors :\t',exer.errors)
    return render(request,"texer_temp.html",{'form' : exer})