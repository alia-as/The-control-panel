from django.shortcuts import render , get_object_or_404
from .forms import exercise_form_tea,exercise_form_tea_grade , exercise_form_stu
from .models import exercise
from django import forms
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def stu_exercises(request , *args,**kwargs):
    all_exer = exercise.objects.all()
    return render(request,"stexer_temp.html",{"all" : all_exer})
def stu_upload_view(request , id , *args , **kwargs):
    exercise_fileee = exercise.objects.get(id=id)

    context = {}
    if request.method == "POST":
        exer = request.FILES["my_file"]
        fs = FileSystemStorage()
        name = fs.save(exer.name, exer)
        context['url'] = fs.url(name)
        exercise_fileee.exercise_file = fs.url(name)
        exercise_fileee.exercise_file_name = exer.name
        exercise_fileee.save()
    return render(request, "exer_upload_temp.html", context)
def tea_add_exer_view(request,*args,**kwargs):
    exer = exercise_form_tea(request.POST or None)
    if request.method == "POST":
        exer = exercise_form_tea(request.POST)
        if exer.is_valid():
            exer.save()
            exer = exercise_form_tea()
        else:
            print('Errors :\t',exer.errors)
    return render(request,"texer_add_temp.html",{'form' : exer})
def tea_exercises(request,*args,**kwargs):
    all_exer = exercise.objects.all()
    return render(request, "texer_temp.html", {"all": all_exer})
def exercise_stu_view(request , id , *args , **kwargs):
    ex = exercise.objects.get(id=id)
    return render(request,"exers_stu_temp.html",{'exercise' : ex})
def exercise_tea_view(request , id , *args , **kwargs):
    ex = exercise.objects.get(id=id)
    return render(request,"exers_tea_temp.html",{'exercise' : ex})